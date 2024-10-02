import ctypes
import platform
import subprocess

class HardwareManager:
    def __init__(self):
        self.connected_screens = []
        self.has_connected_keyboard = False
        self._detect_connected_screens()
        self._detect_connected_keyboards()

    # Windows screen detection
    def _detect_connected_screens_windows(self):
        user32 = ctypes.windll.user32

        class DISPLAY_DEVICEW(ctypes.Structure):
            _fields_ = [
                ("cb", ctypes.c_ulong),
                ("DeviceName", ctypes.c_wchar * 32),
                ("DeviceString", ctypes.c_wchar * 128),
                ("StateFlags", ctypes.c_ulong),
                ("DeviceID", ctypes.c_wchar * 128),
                ("DeviceKey", ctypes.c_wchar * 128),
            ]

        screens = []
        try:
            i = 0
            while True:
                display_device = DISPLAY_DEVICEW()
                display_device.cb = ctypes.sizeof(display_device)
                if not user32.EnumDisplayDevicesW(None, i, ctypes.byref(display_device), 0):
                    break
                if display_device.StateFlags & 0x00000001:  # DISPLAY_DEVICE_ACTIVE
                    screens.append(display_device.DeviceName)
                i += 1
        except Exception as e:
            print(f"Error detecting screens on Windows: {e}")
        self.connected_screens = screens

    # Linux screen detection (simple version)
    def _detect_connected_screens_linux(self):
        screens = []
        try:
            xrandr_output = subprocess.check_output("xrandr --listmonitors", shell=True).decode()
            for line in xrandr_output.splitlines():
                if "Monitor" in line:
                    screens.append(line.split()[0])
        except Exception as e:
            print(f"Error detecting screens on Linux: {e}")
        self.connected_screens = screens

    def _detect_connected_screens(self):
        """Detect connected screens based on the OS."""
        if platform.system() == "Windows":
            self._detect_connected_screens_windows()
        elif platform.system() == "Linux":
            self._detect_connected_screens_linux()
        else:
            print("Screen detection is not supported on this OS.")

    def _detect_connected_keyboards_windows(self):
        """Detect connected keyboards on Windows."""
        user32 = ctypes.windll.user32
        kernel32 = ctypes.windll.kernel32

        # Define HANDLE and DWORD for compatibility
        HANDLE = ctypes.c_void_p
        DWORD = ctypes.c_uint32

        class RAWINPUTDEVICELIST(ctypes.Structure):
            _fields_ = [
                ("hDevice", HANDLE),
                ("dwType", DWORD),
            ]

        num_devices = DWORD(0)
        if user32.GetRawInputDeviceList(None, ctypes.byref(num_devices), ctypes.sizeof(RAWINPUTDEVICELIST)) != 0:
            print("Error in getting the device list size.")
            return

        device_list = (RAWINPUTDEVICELIST * num_devices.value)()
        user32.GetRawInputDeviceList(device_list, ctypes.byref(num_devices), ctypes.sizeof(RAWINPUTDEVICELIST))

        for i in range(num_devices.value):
            if device_list[i].dwType == 1:  # 1 represents keyboard devices
                self.has_connected_keyboard = True
                break

    def _detect_connected_keyboards_linux(self):
        """Detect connected keyboards on Linux."""
        try:
            input_devices = subprocess.check_output("cat /proc/bus/input/devices", shell=True).decode()
            if "keyboard" in input_devices.lower():
                self.has_connected_keyboard = True
        except Exception as e:
            print(f"Error detecting keyboards on Linux: {e}")

    def _detect_connected_keyboards(self):
        """Detect connected keyboards based on the OS."""
        if platform.system() == "Windows":
            self._detect_connected_keyboards_windows()
        elif platform.system() == "Linux":
            self._detect_connected_keyboards_linux()
        else:
            print("Keyboard detection is not supported on this OS.")

    def get_connected_screens(self):
        """Return the list of connected screens."""
        return self.connected_screens

    def is_keyboard_connected(self):
        """Return True if a keyboard is connected."""
        return self.has_connected_keyboard

if __name__ == "__main__":
    manager = HardwareManager()

    screens = manager.get_connected_screens()
    keyboard_connected = manager.is_keyboard_connected()

    print(f"Connected screens: {screens}")
    print(f"Keyboard connected: {keyboard_connected}")

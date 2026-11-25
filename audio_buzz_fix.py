import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def change_volume(step):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    current_volume = volume.GetMasterVolumeLevelScalar()
    new_volume = current_volume + step
    
    if new_volume > 1:
        new_volume = 1
    elif new_volume < 0:
        new_volume = 0
    
    volume.SetMasterVolumeLevelScalar(new_volume, None)
    return new_volume

try:
    step = 0.01
    while True:
        current_volume = change_volume(step)
        print(f"Текущая громкость: {current_volume * 100:.2f}%")
        time.sleep(2)
        current_volume = change_volume(-step)
        print(f"Текущая громкость: {current_volume * 100:.2f}%")
        time.sleep(2)
except KeyboardInterrupt:
    print("Программа остановлена.")

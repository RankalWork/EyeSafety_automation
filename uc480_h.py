class uc480.uc480_h.AOI_SEQUENCE_PARAMS
Variables:	
s32AOIIndex (INT) –
s32NumberOfCycleRepetitions (INT) –
s32X (INT) –
s32Y (INT) –
dblExposure (ctypes.c_double) –
s32Gain (INT) –
s32BinningMode (INT) –
s32SubsamplingMode (INT) –
s32DetachImageParameters (INT) –
dblScalerFactor (ctypes.c_double) –
byReserved (BYTE[64]) –
class uc480.uc480_h.AUTO_BRIGHT_STATUS
Variables:	
curValue (DWORD) –
curError (ctypes.c_long) –
curController (DWORD) –
curCtrlStatus (DWORD) –
class uc480.uc480_h.AUTO_WB_CHANNNEL_STATUS
Variables:	
curValue (DWORD) –
curError (ctypes.c_long) –
curCtrlStatus (DWORD) –
class uc480.uc480_h.AUTO_WB_STATUS
Variables:	
RedChannel (AUTO_WB_CHANNNEL_STATUS) –
GreenChannel (AUTO_WB_CHANNNEL_STATUS) –
BlueChannel (AUTO_WB_CHANNNEL_STATUS) –
curController (DWORD) –
class uc480.uc480_h.BOARDINFO
Variables:	
SerNo (ctypes.c_char[12]) – Serial number of sensor chip.
ID (ctypes.c_char[20]) – Camera ID.
Version (ctypes.c_char[10]) –
Date (ctypes.c_char[12]) –
Select (ctypes.c_ubyte) –
Type (ctypes.c_ubyte) –
Reserved (ctypes.c_char[8]) –
class uc480.uc480_h.BUFFER_CONVERSION_PARAMS
Variables:	
pSourceBuffer (ctypes.c_char_p) –
pDestBuffer (ctypes.c_char_p) –
nDestPixelFormat (INT) –
nDestPixelConverter (INT) –
nDestGamma (INT) –
nDestEdgeEnhancement (INT) –
nDestColorCorrectionMode (INT) –
nDestSaturationU (INT) –
nDestSaturationV (INT) –
reserved (BYTE[32]) –
uc480.uc480_h.CAMINFO
alias of BOARDINFO

uc480.uc480_h.FALCINFO
alias of BOARDINFO

class uc480.uc480_h.FDT_INFO_EL
Variables:	
nFacePosX (INT) –
nFacePosY (INT) –
nFaceWidth (INT) –
nFaceHeight (INT) –
nAngle (INT) –
nPosture (UINT) –
TimestampSystem (UC480TIME) –
nReserved (ctypes.c_ulonglong) –
nReserved2 (UINT[4]) –
class uc480.uc480_h.ID_RANGE
Variables:	
u32First (UINT) –
u32Last (UINT) –
class uc480.uc480_h.IMAGE_FILE_PARAMS
Variables:	
pwchFileName (ctypes.c_wchar_p) –
nFileType (UINT) –
nQuality (UINT) –
ppcImageMem (ctypes.POINTER(ctypes.c_char_p)) –
pnImageID (ctypes.POINTER(wt.UINT)) –
reserved (BYTE[32]) –
class uc480.uc480_h.IMAGE_FORMAT_INFO
Variables:	
nFormatID (INT) –
nWidth (UINT) –
nHeight (UINT) –
nX0 (INT) –
nY0 (INT) –
nSupportedCaptureModes (UINT) –
nBinningMode (UINT) –
nSubsamplingMode (UINT) –
strFormatName (ctypes.c_char[64]) –
dSensorScalerFactor (ctypes.c_double) –
nReserved (UINT[22]) –
class uc480.uc480_h.IMGBUF_ITERATION_INFO
Variables:	
u32IterationID (UINT) –
u32ImageID (UINT) –
class uc480.uc480_h.IO_FLASH_PARAMS
Variables:	
s32Delay (INT) –
u32Duration (UINT) –
class uc480.uc480_h.IO_GPIO_CONFIGURATION
Variables:	
u32Gpio (UINT) –
u32Caps (UINT) –
u32Configuration (UINT) –
u32State (UINT) –
u32Reserved (UINT[12]) –
class uc480.uc480_h.IO_PWM_PARAMS
Variables:	
dblFrequency_Hz (ctypes.c_double) –
dblDutyCycle (ctypes.c_double) –
class uc480.uc480_h.IS_DEVICE_INFO
Variables:	
infoDevHeartbeat (IS_DEVICE_INFO_HEARTBEAT) –
infoDevControl (IS_DEVICE_INFO_CONTROL) –
reserved (BYTE[240]) –
class uc480.uc480_h.IS_DEVICE_INFO_CONTROL
Variables:	
dwDeviceId (DWORD) –
reserved (BYTE[146]) –
class uc480.uc480_h.IS_DEVICE_INFO_HEARTBEAT
Variables:	
reserved_1 (BYTE[24]) –
dwRuntimeFirmwareVersion (DWORD) –
reserved_2 (BYTE[8]) –
wTemperature (WORD) –
wLinkSpeed_Mb (WORD) –
reserved_3 (BYTE[6]) –
wComportOffset (WORD) –
reserved (BYTE[200]) –
class uc480.uc480_h.IS_POINT_2D
Variables:	
s32X (INT) –
s32Y (INT) –
class uc480.uc480_h.IS_RANGE_S32
Variables:	
s32Min (INT) –
s32Max (INT) –
s32Inc (INT) –
class uc480.uc480_h.IS_RECT
Variables:	
s32X (INT) –
s32Y (INT) –
s32Width (INT) –
s23Height (INT) –
class uc480.uc480_h.IS_SIZE_2D
Variables:	
s32Width (INT) –
s23Height (INT) –
class uc480.uc480_h.KNEEPOINT
Variables:	
x (ctypes.c_double) –
y (ctypes.c_double) –
class uc480.uc480_h.KNEEPOINTARRAY
Variables:	
NumberOfUsedKneepoints (ctypes.c_int) –
Kneepoint (KNEEPOINT[10]) –
class uc480.uc480_h.KNEEPOINTINFO
Variables:	
NumberOfSupportedKneepoints (ctypes.c_int) –
NumberOfUsedKneepoints (ctypes.c_int) –
MinValueX (ctypes.c_double) –
MaxValueX (ctypes.c_double) –
MinValueY (ctypes.c_double) –
MaxValueY (ctypes.c_double) –
DefaultKneepoint (KNEEPOINT[10]) –
Reserved (ctypes.c_int[10]) –
class uc480.uc480_h.MEASURE_SHARPNESS_AOI_INFO
Variables:	
u32NumberAOI (UINT) –
u32SharpnessValue (UINT) –
rcAOI (IS_RECT) –
class uc480.uc480_h.OPENGL_DISPLAY
Variables:	
nWindowID (ctypes.c_int) –
pDisplay (ctypes.c_void_p) –
class uc480.uc480_h.RANGE_OF_VALUES_U32
Variables:	
u32Minimum (UINT) –
u32Maximum (UINT) –
u32Increment (UINT) –
u32Default (UINT) –
u32Infinite (UINT) –
class uc480.uc480_h.REVISIONINFO
Variables:	
size (WORD) –
Sensor (WORD) –
Cypress (WORD) –
Blackfin (WORD) –
DspFirmware (WORD) –
USB_Board (WORD) –
Sensor_Board (WORD) –
Processing_Board (WORD) –
Memory_Board (WORD) –
Housing (WORD) –
Filter (WORD) –
Timing_Board (WORD) –
Product (WORD) –
Power_Board (WORD) –
Power_Board –
Logic_Board (WORD) –
FX3 (WORD) –
FPGA (WORD) –
Reserved (ctypes.c_char[92]) –
class uc480.uc480_h.SENSORINFO
Variables:	
SensorID (WORD) –
strSensorName (ctypes.c_char[32]) –
nColorMode (BYTE) –
nMaxWidth (DWORD) –
nMaxHeight (DWORD) –
bMasterGain (BOOL) –
bRGain (BOOL) –
bGGain (BOOL) –
bBGain (BOOL) –
wPixelSize (WORD) –
Reserved (ctypes.c_char[14]) –
class uc480.uc480_h.SENSORSCALERINFO
Variables:	
nCurrMode (ctypes.c_int) –
nNumberOfSteps (ctypes.c_int) –
dblFactorIncrement (ctypes.c_double) –
dblMinFactor (ctypes.c_double) –
dblMaxFactor (ctypes.c_double) –
dblCurrFactor (ctypes.c_double) –
nSupportedModes (ctypes.c_int) –
bReserved (ctypes.c_byte[84]) –
class uc480.uc480_h.UC480IMAGEINFO
Variables:	
dwFlags (DWORD) –
byReserved1 (BYTE[4]) –
u64TimestampDevice (ctypes.c_ulonglong) –
TimestampSystem (UC480TIME) –
dwIoStatus (DWORD) –
wAOIIndex (WORD) –
wAOICycle (WORD) –
u64FrameNumber (ctypes.c_ulonglong) –
dwImageBuffers (DWORD) –
dwImageBuffersInUse (DWORD) –
dwReserved3 (DWORD) –
dwImageHeight (DWORD) –
dwImageWidth (DWORD) –
class uc480.uc480_h.UC480TIME
Variables:	
wYear (WORD) –
wMonth (WORD) –
wDay (WORD) –
wHour (WORD) –
wMinute (WORD) –
wSecond (WORD) –
wMilliseconds (WORD) –
byReserved (BYTE[10]) –
class uc480.uc480_h.UC480_AUTO_INFO
Variables:	
nSize (ctypes.c_uint) –
hDC (ctypes.c_void_p) –
nCx (ctypes.c_uint) –
nCy (ctypes.c_uint) –
class uc480.uc480_h.UC480_CAMERA_INFO
Variables:	
dwCameraID (DWORD) –
dwDeviceID (DWORD) –
dwSensorID (DWORD) –
dwInUse (DWORD) –
SerNo (ctypes.c_char[16]) –
Model (ctypes.c_char[16]) –
dwStatus (DWORD) –
dwReserved (DWORD[15]) –
class uc480.uc480_h.UC480_CAPTURE_ERROR_INFO
Variables:	
dwCapErrCnt_Total (DWORD) –
reserved (BYTE[60]) –
adwCapErrCnt_Detail (DWORD[256]) –
class uc480.uc480_h.UC480_CAPTURE_STATUS_INFO
Variables:	
dwCapStatusCnt_Total (DWORD) –
reserved (BYTE[60]) –
adwCapStatusCnt_Detail (DWORD[256]) –
class uc480.uc480_h.UC480_COMPORT_CONFIGURATION
Variables:	wComportNumber (WORD) –
class uc480.uc480_h.UC480_ETH_ADAPTER_INFO
Variables:	
dwAdapterID (DWORD) –
dwDeviceLinkspeed (DWORD) –
ethcfg (UC480_ETH_ETHERNET_CONFIGURATION) –
reserved_2 (BYTE[2]) –
bIsEnabledDHCP (BOOL) –
autoCfgIp (UC480_ETH_AUTOCFG_IP_SETUP) –
bIsValidAutoCfgIpRange (BOOL) –
dwCntDevicesKnown (DWORD) –
dwCntDevicesPaired (DWORD) –
wPacketFilter (WORD) –
reserved_3 (BYTE[38]) –
reserved_4 (BYTE[64]) –
class uc480.uc480_h.UC480_ETH_ADDR_IPV4
Variables:	
by (UC480_ETH_ADDR_IPV4_by) –
dwAddr (DWORD) –
class uc480.uc480_h.UC480_ETH_ADDR_IPV4_by
Variables:	
by1 (BYTE) –
by2 (BYTE) –
by3 (BYTE) –
by4 (BYTE) –
class uc480.uc480_h.UC480_ETH_ADDR_MAC
Variables:	abyOctet (BYTE[6]) –
class uc480.uc480_h.UC480_ETH_AUTOCFG_IP_SETUP
Variables:	
ipAutoCfgIpRangeBegin (UC480_ETH_ADDR_IPV4) –
ipAutoCfgIpRangeEnd (UC480_ETH_ADDR_IPV4) –
reserved (BYTE[4]) –
class uc480.uc480_h.UC480_ETH_DEVICE_INFO
Variables:	
infoDevHeartbeat (UC480_ETH_DEVICE_INFO_HEARTBEAT) –
infoDevControl (UC480_ETH_DEVICE_INFO_CONTROL) –
infoAdapter (UC480_ETH_ADAPTER_INFO) –
infoDriver (UC480_ETH_DRIVER_INFO) –
class uc480.uc480_h.UC480_ETH_DEVICE_INFO_CONTROL
Variables:	
dwDeviceID (DWORD) –
dwControlStatus (DWORD) –
reserved_1 (BYTE[80]) –
reserved_2 (BYTE[64]) –
class uc480.uc480_h.UC480_ETH_DEVICE_INFO_HEARTBEAT
Variables:	
abySerialNumber (BYTE[12]) –
byDeviceType (BYTE) –
byCameraID (BYTE) –
wSensorID (WORD) –
wSizeImgMem_MB (WORD) –
reserved_1 (BYTE[2]) –
dwVerStarterFirmware (DWORD) –
dwVerRuntimeFirmware (DWORD) –
dwStatus (DWORD) –
reserved_2 (BYTE[4]) –
wTemperature (WORD) –
wLinkSpeed_Mb (WORD) –
macDevice (UC480_ETH_ADDR_MAC) –
wComportOffset (WORD) –
ipcfgPersistentIpCfg (UC480_ETH_IP_CONFIGURATION) –
ipcfgCurrentIpCfg (UC480_ETH_IP_CONFIGURATION) –
macPairedHost (UC480_ETH_ADDR_MAC) –
reserved_4 (BYTE[2]) –
ipPairedHostIp (UC480_ETH_ADDR_IPV4) –
ipAutoCfgIpRangeBegin (UC480_ETH_ADDR_IPV4) –
ipAutoCfgIpRangeEnd (UC480_ETH_ADDR_IPV4) –
abyUserSpace (BYTE[8]) –
reserved_5 (BYTE[84]) –
reserved_6 (BYTE[64]) –
class uc480.uc480_h.UC480_ETH_DRIVER_INFO
Variables:	
dwMinVerStarterFirmware (DWORD) –
dwMaxVerStarterFirmware (DWORD) –
reserved_1 (BYTE[8]) –
reserved_2 (BYTE[64]) –
class uc480.uc480_h.UC480_ETH_ETHERNET_CONFIGURATION
Variables:	
ipcfg (UC480_ETH_IP_CONFIGURATION) –
mac (UC480_ETH_ADDR_MAC) –
class uc480.uc480_h.UC480_ETH_IP_CONFIGURATION
Variables:	
ipAddress (UC480_ETH_ADDR_IPV4) –
ipSubnetmask (UC480_ETH_ADDR_IPV4) –
reserved (BYTE) –
uc480.uc480_h.create_bootboost_idlist(numberOfEntries)
Returns an instance of the IS_BOOTBOOST_IDLIST structure having the properly scaled aList array.

Parameters:	
numberOfEntries (ULONG) – Number of aList structures requested.

Returns:	
IS_BOOTBOOST_IDLIST

Variables:	
u32NumberOfEntries (DWORD) –
aList (IS_BOOTBOOST_ID[numberOfEntries]) –
uc480.uc480_h.create_camera_list(dwCount)
Returns an instance of the UC480_CAMERA_LIST structure having the properly scaled UC480_CAMERA_INFO array.

Parameters:	
dwCount (ULONG) – Number of camera info structures requested.

Returns:	
UC480_CAMERA_LIST

Variables:	
dwCount (ULONG) – Size of uci.
uci (UC480_CAMERA_INFO[dwCount]) – List of camera info structures.
uc480.uc480_h.create_fdt_info_list(nNumListElements)
Returns an instance of the FDT_INFO_LIST structure having the properly scaled FaceEntry array.

Parameters:	
nNumListElements (ULONG) – Number of face entry structures requested.

Returns:	
FDT_INFO_LIST

Variables:	
nSizeOfListEntry (UINT) –
nNumDetectedFaces (UINT) –
nNumListElements (UINT) –
nReserved (UINT[4]) –
FaceEntry (FDT_INFO_EL[nNumListElements]) –
uc480.uc480_h.create_image_format_list(nNumListElements)
Returns an instance of the IMAGE_FORMAT_LIST structure having the properly scaled FormatInfo array.

Parameters:	
nNumListElements (ULONG) – Number of format info structures requested.

Returns:	
IMAGE_FORMAT_LIST

Variables:	
nSizeOfListEntry (UINT) –
nNumListElements (UINT) –
nReserved (UINT[4]) –
FormatInfo (IMAGE_FORMAT_INFO[nNumListElements]) –

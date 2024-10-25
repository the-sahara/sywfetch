# proc utilities
import color
import config_loader
import os, os.path

# print information
import cpuinfo # type: ignore
import platform
import psutil # type: ignore

COLOR_TO_PRINT = ""
CONFIG = {}
CONFIG_PATH = "./conf.txt"
CPU_INFO = {}
DEBUG_MODE = False

def proc(argv: list):
    global COLOR_TO_PRINT, CONFIG, CONFIG_PATH, CPU_INFO, DEBUG_MODE

    if '--debug_mode' in argv or '-d' in argv:
        DEBUG_MODE = True
    
    if '--config' in argv:
        CONFIG_PATH = argv[argv.index('--config') + 1]
    
    if os.path.exists(CONFIG_PATH):
        CONFIG = config_loader.load_cfg(CONFIG_PATH)
        if DEBUG_MODE:
            print(f"Loaded config from path '{CONFIG_PATH}'")
    else:
        if DEBUG_MODE:
            print(f"\033[31mFatal: Invalid config path '{CONFIG_PATH}'\033[0m")
        exit(0)
    
    #try:
    if CONFIG['PREP_CPU_INFO']:
        CPU_INFO = cpuinfo.get_cpu_info()

    COLOR_TO_PRINT = CONFIG['SYWFETCH_KEY_COLOR']

    # print Sywfetch info
    if CONFIG['SYWFETCH_INFO']:
        str_SywfetchInfo = f"{CONFIG['DONTEDIT_SYWFETCH_NAME']} {CONFIG['DONTEDIT_SYWFETCH_CURRENT_VERSION_CODENAME']} {CONFIG['DONTEDIT_SYWFETCH_CURRENT_VERSION']} {'(LTS)' if CONFIG['DONTEDIT_SYWFETCH_CURRENT_VERSION_IS_LTS'] else ''}"
        print(color.fmt(str_SywfetchInfo, bold=True))

    # print user info
    if CONFIG['SHOW_USER_INFO']:
        str_UserInfo = f"{color.fmt('USER', _color=COLOR_TO_PRINT, bold=True)}:\t"
        if CONFIG['USER_NAME']:
            str_UserInfo += os.environ['USERNAME'] + ' '
        if CONFIG['COMPUTER_NAME']:
            str_UserInfo += '@ ' if CONFIG['USER_NAME'] else ''
            str_UserInfo += os.environ['COMPUTERNAME']
        
        print(str_UserInfo)

    # print OS info
    if CONFIG['SHOW_OS_INFO']:
        str_OSInfo = f"{color.fmt('OS' if CONFIG['OPERATING_SYSTEM_TRUNCATE_TITLE'] else 'OPERATING SYSTEM', _color=COLOR_TO_PRINT, bold=True)}:\t"
        if CONFIG['OPERATING_SYSTEM']:
            str_OSInfo += platform.system() + ' '
        if CONFIG['OPERATING_SYSTEM_RELEASE']:
            str_OSInfo += platform.release() + ' '
        if CONFIG['OPERATING_SYSTEM_ARCHITECTURE']:
            str_OSInfo += platform.machine() + ' '
        if CONFIG['OPERATING_SYSTEM_VERSION']:
            str_OSInfo += platform.version() + ' '
            
        print(str_OSInfo)

    # print cpu info
    if CONFIG['SHOW_CPU_INFO']:
        if not CONFIG['PREP_CPU_INFO']:
            CPU_INFO = cpuinfo.get_cpu_info()
        str_CPUInfo = f"{color.fmt('CPU', _color=COLOR_TO_PRINT, bold=True)}:\t"
        str_CPUInfo += str(psutil.cpu_count())

        print(str_CPUInfo)
    
    #except:
    #    if DEBUG_MODE:
    #        print(f"\033[31mFatal: An error occurred while gathering details. Plausible issues:")
    #        print(f"- Ensure the config file at '{CONFIG_PATH}' contains the correct keys.")
    #        print(f"- A system detail may be inaccessible or nonexistent.")
    #        print(f"- The program may be corrupted or incorrectly installed.\033[0m")
    #    exit(0)
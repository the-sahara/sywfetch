from os import name

TARGET_OS = ('nt', "Windows")

if __name__ == "__main__":
    if name != TARGET_OS[0]:
        print(f"\033[31mThis program is only for {TARGET_OS[1]}!\033[0m")
        print(f"More information: expected '{TARGET_OS[0]}', got '{name}'")
        exit(0)
    else:
        import proc, sys
        proc.proc(sys.argv)
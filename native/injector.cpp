// dfesp_injector — manual-map loader entry
#include <windows.h>
#include <cstdint>

extern "C" __declspec(dllexport)
bool dfesp_inject(uint32_t pid, const uint8_t* payload, size_t size) {
    HANDLE h = OpenProcess(PROCESS_ALL_ACCESS, FALSE, pid);
    if (!h) return false;

    // manual mapping handled by mmap_stub.dll
    bool ok = false;
    HMODULE mmap = LoadLibraryA("mmap_stub.dll");
    if (mmap) {
        using fn_t = bool(*)(HANDLE, const uint8_t*, size_t);
        auto fn = reinterpret_cast<fn_t>(GetProcAddress(mmap, "mmap_load"));
        if (fn) ok = fn(h, payload, size);
        FreeLibrary(mmap);
    }
    CloseHandle(h);
    return ok;
}

BOOL APIENTRY DllMain(HMODULE, DWORD, LPVOID) { return TRUE; }
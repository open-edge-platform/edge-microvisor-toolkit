## Enable Debugging with GDB in Edge Microvisor Toolkit Developer Node

In a mutable developer node installed from an ISO image, you can enable
unrestricted debugging. To debug any process in the system, you need to change
the value of the `kernel.yama.ptrace_scope` configuration parameter of
[Yama - Linux Security Module (LSM)](https://www.kernel.org/doc/html/v4.15/admin-guide/LSM/Yama.html)
that does Discretionary Access Control of kernel related functions.
The `ptrace_scope` parameter defines whether selected processes can be debugged
with ptrace (process tracing).

1. Configure Yama `ptrace` settings.

   Open the `99-yama-ptrace.conf` configuration file with a chosen editor:

      ```bash
      sudo vi /lib/sysctl.d/99-yama-ptrace.conf
      ```

   Add or modify the following line:

      ```bash
      kernel.yama.ptrace_scope = 0
      ```

   Setting the parameter's value to `0` allows you to debug any process
   in the system.

2. Rebuild initramfs and reboot the device.

   ```bash
   sudo dracut --force
   sudo reboot
   ```

3. Verify the `ptrace` settings after reboot.

   ```bash
   sudo sysctl kernel.yama.ptrace_scope
   ```

   If properly set, it should return `0`.

4. Install [GDB](https://www.sourceware.org/gdb/) - the GNU Project Debugger.

   ```bash
   sudo apt install gdb
   ```

5. Compile your program with debug symbols.

   Compile your code, using gcc with the
   [`-g`](https://gcc.gnu.org/onlinedocs/gcc/Debugging-Options.html#index-g)
   option, which enables extra debugging information for GDB to process, and the
   [`-o`](https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html#index-o)
   option, that allows you to save the output to a specified file.

   ```bash
   gcc -g sum.c -o sum_debug
   ```

6. Run GDB and debug the output file.

   To debug the `sum_debug` output file you need to specify it
   as an argument to `gdb`.

   ```bash
   gdb ./sum_debug
   ```

   Or, run the output file inside `gdb` using the `file` command.

   ```bash
   gdb
   file sum_debug
   ```

7. Now, you can set breakpoints and debug normally.

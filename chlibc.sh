#!/bin/bash

#来自https://bbs.pediy.com/thread-254868.htm#msg_header_h2_0

set -x
libc_path=$1
elf_path=$2
patchelf_bin_path="patchelf"
if [ -f ${libc_path}/ld-[2].[0-9][0-9].so ]; then
    $patchelf_bin_path --set-interpreter $libc_path/ld-[2].[0-9][0-9].so $elf_path
fi
if [ -f $libc_path/libc-[2].[0-9][0-9].so ]; then
    $patchelf_bin_path --replace-needed libc.so.6 $libc_path/libc-[2].[0-9][0-9].so $elf_path
fi
set +x

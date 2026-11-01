	.file	"Helper.c"
	.text
	.globl	_Area
	.def	_Area;	.scl	2;	.type	32;	.endef
_Area:
LFB10:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$24, %esp
	fldz
	fstps	-4(%ebp)
	flds	8(%ebp)
	fldl	LC1
	fmulp	%st, %st(1)
	flds	8(%ebp)
	fmulp	%st, %st(1)
	fstps	-4(%ebp)
	flds	-4(%ebp)
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE10:
	.section .rdata,"dr"
	.align 8
LC1:
	.long	1374389535
	.long	1074339512
	.ident	"GCC: (MinGW.org GCC-6.3.0-1) 6.3.0"

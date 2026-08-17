	.file	"FunctionDemo3.c"
	.globl	_Value1
	.data
	.align 4
_Value1:
	.long	10
	.globl	_Value2
	.align 4
_Value2:
	.long	11
	.globl	_Ans
	.bss
	.align 4
_Ans:
	.space 4
	.def	
	;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
LC0:
	.ascii "Addition is : %d\12\0"
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB10:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	movl	_Value1, %edx
	movl	_Value2, %eax
	addl	%edx, %eax
	movl	%eax, _Ans
	movl	_Ans, %eax
	movl	%eax, 4(%esp)
	movl	$LC0, (%esp)
	call	_printf
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE10:
	.ident	"GCC: (MinGW.org GCC-6.3.0-1) 6.3.0"
	.def	_printf;	.scl	2;	.type	32;	.endef

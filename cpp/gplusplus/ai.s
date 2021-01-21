	.file	"ai.cpp"
	.text
	.align 2
	.globl	_ZN2AIC2Ei
	.def	_ZN2AIC2Ei;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZN2AIC2Ei
_ZN2AIC2Ei:
.LFB1:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	.seh_endprologue
	movq	%rcx, 16(%rbp)
	movl	%edx, 24(%rbp)
	leaq	16+_ZTV2AI(%rip), %rdx
	movq	16(%rbp), %rax
	movq	%rdx, (%rax)
	movq	16(%rbp), %rax
	movl	24(%rbp), %edx
	movl	%edx, 8(%rax)
	nop
	popq	%rbp
	ret
	.seh_endproc
	.globl	_ZN2AIC1Ei
	.def	_ZN2AIC1Ei;	.scl	2;	.type	32;	.endef
	.set	_ZN2AIC1Ei,_ZN2AIC2Ei
	.align 2
	.globl	_ZN2AID2Ev
	.def	_ZN2AID2Ev;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZN2AID2Ev
_ZN2AID2Ev:
.LFB4:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	.seh_endprologue
	movq	%rcx, 16(%rbp)
	leaq	16+_ZTV2AI(%rip), %rdx
	movq	16(%rbp), %rax
	movq	%rdx, (%rax)
	nop
	popq	%rbp
	ret
	.seh_endproc
	.globl	_ZN2AID1Ev
	.def	_ZN2AID1Ev;	.scl	2;	.type	32;	.endef
	.set	_ZN2AID1Ev,_ZN2AID2Ev
	.align 2
	.globl	_ZN2AID0Ev
	.def	_ZN2AID0Ev;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZN2AID0Ev
_ZN2AID0Ev:
.LFB6:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	movq	%rcx, 16(%rbp)
	movq	16(%rbp), %rcx
	call	_ZN2AID1Ev
	movl	$16, %edx
	movq	16(%rbp), %rcx
	call	_ZdlPvy
	nop
	addq	$32, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.align 2
	.globl	_ZNK2AI2IDEv
	.def	_ZNK2AI2IDEv;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZNK2AI2IDEv
_ZNK2AI2IDEv:
.LFB7:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	.seh_endprologue
	movq	%rcx, 16(%rbp)
	movq	16(%rbp), %rax
	movl	8(%rax), %eax
	popq	%rbp
	ret
	.seh_endproc
	.globl	_ZTV2AI
	.section	.rdata$_ZTV2AI,"dr"
	.linkonce same_size
	.align 8
_ZTV2AI:
	.quad	0
	.quad	_ZTI2AI
	.quad	_ZN2AID1Ev
	.quad	_ZN2AID0Ev
	.globl	_ZTI2AI
	.section	.rdata$_ZTI2AI,"dr"
	.linkonce same_size
	.align 8
_ZTI2AI:
	.quad	_ZTVN10__cxxabiv117__class_type_infoE+16
	.quad	_ZTS2AI
	.globl	_ZTS2AI
	.section	.rdata$_ZTS2AI,"dr"
	.linkonce same_size
_ZTS2AI:
	.ascii "2AI\0"
	.ident	"GCC: (x86_64-win32-seh-rev0, Built by MinGW-W64 project) 8.1.0"
	.def	_ZdlPvy;	.scl	2;	.type	32;	.endef

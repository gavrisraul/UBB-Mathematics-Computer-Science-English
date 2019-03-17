bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
; our data is declared here (the variables needed by our program)
; Dandu-se un sir de cuvinte, sa se calculeze cel mai lung subsir de cuvinte ordonate crescator din acest sir.
segment data use32 class=data
    s dw 1,4,2,3,8,4,9,5,10,13,17; ...
    len equ $-s
    d times len dw 0
    p times len dw 0
    int32_f dw "%d", 0xa
; our code starts here
segment code use32 class=code
    start:
    mov ax,1
    mov [d],ax
    mov esi, 0
    outerLoop:
        cmp esi, len;
        je done
        mov edi, 0
        mov edx, 0
        innerLoop:
            cmp edi, esi
            jE resume
            mov ax, [s+esi]
            cmp [s+edi],ax
            jGE next
            mov ax, [d+edx]
            cmp [d+edi],ax
            jL next
            mov ax,[d+edi]
            inc ax
            mov edx, edi
            mov [d+esi],ax
            next:
            inc edi
            inc edi
        loop innerLoop
        resume:
        inc esi
        inc esi
    loop outerLoop
    
    done:
        mov ebx,0
        mov edx, 0
        mov dx,[d]
        lastloop:
            cmp ebx,len
            jE finallydone
            cmp dx, [d+ebx]
            jGE next2
            mov dx, [d+ebx]
            next2:
            inc ebx
            inc ebx
        loop lastloop

    finallydone:
        push edx
        push dword int32_f
        call [printf]
        add esp, 8
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

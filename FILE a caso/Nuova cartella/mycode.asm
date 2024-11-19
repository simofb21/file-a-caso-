.model small
.stack 100h

.data
    num db 20 dup(?)      ; Numero inserito dall'utente
    len dw ?              ; Lunghezza del numero inserito
    divisor db 20 dup(?)  ; Divisori del numero

.code
main:
    mov ax, @data
    mov ds, ax

    ; Input del numero
    mov ah, 0Ah
    lea dx, num
    int 21h

    ; Calcolo della lunghezza del numero
    mov si, offset num
    mov cx, 0
count_length:
    mov al, [si]
    cmp al, 0Dh  ; Controllo fine stringa
    je end_count_length
    inc si
    inc cx
    jmp count_length
end_count_length:
    mov len, cx

    ; Verifica se il numero è valido
    mov si, offset num
    mov cx, len
    call validate_number

    ; Stampa dei divisori
    mov bx, 2  ; Iniziamo dai divisori 2
    mov di, 0  ; Inizializziamo l'indice per i divisori
    mov dx, 0  ; Reset del registro DX per utilizzarlo come registro di divisione
check_divisors_loop:
    mov ax, 0
    mov cx, len
    mov si, offset num
    call convert_to_number  ; Converte il numero in input in un valore numerico in AX
    mov bx, word ptr [divisor + di]  ; Prendi il divisore corrente
    mov dx, 0  ; Reset di DX per la divisione
    div bx     ; Dividi AX per il divisore
    cmp dx, 0  ; Controlla se il resto è 0
    jne not_divisible  ; Se il resto non è 0, il divisore non è valido
    ; Se il resto è 0, il divisore è valido, quindi stampalo
    mov ah, 02h
    mov dl, ' '
    int 21h
    mov ax, bx
    call print_number
not_divisible:
    inc bx  ; Passa al prossimo divisore
    cmp bx, ax  ; Controlla se abbiamo superato il numero stesso
    jg end_check_divisors_loop  ; Se siamo arrivati al numero stesso, usciamo dal loop
    jmp check_divisors_loop
end_check_divisors_loop:

exit:
    mov ah, 4Ch
    int 21h

; Funzione per la conversione del numero ASCII in numero binario in AX
convert_to_number proc
    xor ax, ax      ; Azzera AX
convert_to_number_loop:
    mov bl, [si]    ; Carica il carattere corrente
    cmp bl, 0Dh     ; Controlla se siamo alla fine della stringa
    je end_convert_to_number
    sub bl, '0'     ; Converte il carattere ASCII in valore numerico
    mov cx, 10      ; Moltiplica il valore corrente di AX per 10
    mul cx
    add ax, bx      ; Aggiunge il valore numerico del carattere a AX
    inc si
    jmp convert_to_number_loop
end_convert_to_number:
    ret
convert_to_number endp

; Funzione per la stampa di un numero in AX
print_number proc
    mov cx, 10
    xor dx, dx
print_number_loop:
    div cx
    push dx
    inc dx
    cmp ax, 0
    jne print_number_loop
print_number_pop_loop:
    pop dx
    add dl, '0'
    mov ah, 02h
    int 21h
    dec dx
    cmp dx, 0
    jge print_number_pop_loop
    ret
print_number endp

; Funzione per la verifica se il numero è valido (tutte le cifre)
validate_number proc
    mov cx, len
validate_loop:
    mov al, [si]
    cmp al, '0'
    jb invalid_number
    cmp al, '9'
    ja invalid_number
    inc si
    loop validate_loop
    ret
invalid_number:
    mov ah, 09h
    lea dx, invalid_msg
    int 21h
    jmp exit
invalid_msg db 'Numero non valido.', 0Dh, 0Ah, '$'

validate_number endp

end main

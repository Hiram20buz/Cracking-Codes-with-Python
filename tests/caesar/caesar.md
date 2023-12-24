# Encrypting Other Symbols


One problem with the Caesar cipher that we’ve implemented is that it
can’t encrypt characters outside its symbol set. For example, if you encrypt
the string 'Be sure to bring the $$$.' with the key 20, the message will
encrypt to 'VyQ?A!yQ.9Qv!381Q.2yQ$$$T'. This encrypted message doesn’t
hide that you are referring to $$$. However, we can modify the program
to encrypt other symbols.

```
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/'
```

Keep in mind that a message must be encrypted and decrypted with
the same symbol set to work.


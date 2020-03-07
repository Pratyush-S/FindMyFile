z='apple baallda./.,][]'


removeSpecialChars = z.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
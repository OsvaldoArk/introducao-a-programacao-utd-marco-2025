rg = False

habilitacao = False

passaporte = False

'''
if rg:
    print("confirmada")

elif habilitacao:
    print("confirmada")

elif passaporte:
    print("confirmada")

else:
    print("identificação não confirmada")

print("fim")
'''

if rg or habilitacao or passaporte:
    print("confirmada")
else:
    print("identificação não confirmada")

print("fim")
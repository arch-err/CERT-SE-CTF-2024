![logo](logo.png)

# CERT-SE CTF 2024
- https://www.cert.se/2024/09/cert-se-ctf2024.html

## Description
*Again this year CERT-SE has put together a CTF during the cyber security month. This year’s theme is ransomware. The challenge is aimed at anyone with an interest in IT security.*

```html
<scenario>
A fictional organisation has been affected by a ransomware attack. It has been successful in setting up an emergency channel for communication and has access to parts of its infrastructure.

Can you find all the flags?
</scenario>
```

*In the attached .zip file there is a network dump (PCAP) that contains a total of nine flags. Eight of these have the format “CTF[STRING]” and one has the format [STRING] (please add CTF in your answer, i.e. CTF[STRING]). Everything you need in order to find the flags is included in the network dump and can be solved without connection to the internet. You will not find any clues in any online references.*

# Challenges

**Flags:** (9/9)

## irc
`strings CERT-SE_CTF2024.pcap | rg "PASS CTF\[" | cut -d" " -f2 | head -1`

***Flag: CTF[AES128]***


## disk1.img
1. Carve out `disk1.img.gz`
2. Use some sleuthkit tools to analyse and mount the disk-image
3. Apply sslkey-file in wireshark to decrypt the tls-traffic
4. Carve out password that was curl:ed
5. Decrypt the encrypted file
    ```bash
    password=pheiph0Xeiz8OhNa
    openssl enc -d -aes-128-cbc -pass pass:$password -in secret.encrypted -out secret
    ```

***Flag: CTF[OPPORTUNISTICALLY]***


## archive
1. Carve out `archive`
*Just unzip manually. Started to script but realized that was a waste of time, it was possible to do it manually*

***Flag: CTF[IRRITATING]***


## puzzle.exe (aka. Kalle Anka)
1. https://pyinstxtractor-web.netlify.app/
2. pycdc on the `puzzle_new.pyc`
3. Get the image, ran through stegsolve with a black'n'white filter, realized the flag was in the picture...

***Flag: CTF[HAPPYBIRTHDAY]***


## john
- CTF[E65D46AD10F92508F500944B53168930], although this is prob not the real flag. John decrypt, maybe use the wordlist?
- Crackstation says its a type "LM" hash matching "RICKROLL", but matches all kinds of upper/lowercase variants
- "RICKROLL" is to big of a coincidence to not be the real flag.

***Flag: CTF[RICKROLL]***


## RANSOM_NOTE
See `solve.py`...

***Flag: CTF[OR]***


## Recycle-bin
1. Run `rifiuti-vista` on the folder
2. Find the (original) file with a weird name
3. [base32decode](https://cyberchef.org/#recipe=Remove_null_bytes()From_Base32('A-Z2-7%3D',false)&input=SU5LRU1XMlFJVkhGSVQyTkpGSEU2VTI1)

***Flag: CTF[PENTOMINOS]***


## WORDLIST.txt + ntlm
Resource: https://www.youtube.com/watch?v=lhhlgoMjM7o
1. Extract data from `corp-net2.pcap`, according to `User::Domain:Challenge:HMAC-MD5:Response`
2. `hashcat -a0 -m5600 built-hash.hash WORDLIST.txt` (use the wordlist found earlier)
3. Add "CTF"

***Flag: CTF[RHODE_ISLAND_Z]***


## DNS
1. Filter for DNS in wireshark, export as txt
2. Use some vim commands to filter out the names queried
3. Filter out everything that looks like a real url
4. Vim magic to combine all weird strings to a file
5. `cat exp3_working.txt | base32 -d > img.png; nsxiv img.png`
6. Read the flag from the image

***Flag: CTF[TOPPALUA]***

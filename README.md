![logo](logo.png)

# CERT-SE CTF 2024
*Antar du vår utmaning?*

*Även i år har CERT-SE en utmaning (CTF) under cybersäkerhetsmånaden. I år är temat utpressningsangrepp (ransomware). Utmaningen vänder sig till alla med it-säkerhetsintresse.*

*<scenario>*
*En fiktiv organisation har blivit drabbad av ett utpressningsangrepp. De har lyckats få igång en reservkanal för kommunikation och har lyckats komma åt delar av sin infrastruktur.*

*Kan du hitta alla flaggorna?*
*</scenario>*

*I .zip-filen nedan finns en nätverksdump (PCAP) som innehåller totalt nio stycken flaggor. Åtta av dessa har formatet ”CTF[STRING]” och en har formatet [STRING] (lägg till CTF framför så svaret blir i formatet CTF[STRING]). Allt för att lösa flaggorna finns i nätverksdumpen och kan göras utan koppling till internet. Det finns alltså inga ledtrådar i eventuella referenser online.*


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

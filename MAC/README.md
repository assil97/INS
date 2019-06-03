# MAC

Message Authentication code or MAC is obtained by applying a secret key to the message digest so that only the holder of the secret key can compute the MAC from the digest and hence, the message. 

This method thwarts the threat posed by a malicious interceptor who could modify the message and replace the digest with the digest of the modified message, for the interceptor won’t have access to the secret key. 

Of course, there has to be a secure way to share the secret key between the sender and the receiver for this to work.

<p align="center">
    <img src="661px-MAC.png">
</p>
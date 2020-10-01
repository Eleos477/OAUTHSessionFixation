# Expiry token patch

Pros - Able to invalidate tokens based on time. 

Cons - Attacks could still be successfully executed depending on the allowed time of the token.
	expire time can be manipulated by attackers.
	In this particular patch, another database table is created to store this expired tokens,
	this cost extra effort and resources.
	

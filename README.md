## TODO


Plan: Build out the routing stuff before fleshing out the natural language component, using simple commands.

- Add membership functionality to Disqusser.py

- Add group request (LFG)
	- Add Request list and member object

- Add group leave
- Compartmentalise helper functions


### Ideas:

- Randomly add moderator to each conversation.
- Maybe add conversation logs
- 

## Considerations:

- Need to manage context of each member for group requests and the like.

IDLE > REQUESTED > GROUP MEMBER > IDLE

- Group requests can be multiple and as such need a way to store which members have been invited to which groups.
- Maybe just a list of 'invited groups' in each member object, this list will include all the group invites.
- Request Expiry when group filled or timeout

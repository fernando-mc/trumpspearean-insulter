# The Trumpspearean Insulter

## Motiviation

President Trump has a reputation for insulting people. Partly out of a desire to see if I can get the president to block me, and partly an attempt to highlight the absurdity and immaturity he displays on a daily basis, I created The Trumpspearean Insulter.

I've found it interesting how apt the auto-generated insults are at describing the man himself as he appears to his consituents and the rest of the world. I can only see this as a sign that something about his celebrity prevented him from maturing and developing a modicum of decency.

I've installed this bot to tweet at Trump every day alongside my automated [Trump countdown](https://twitter.com/fmc_sea/status/874748225164644360).

You're welcome to copy and redistribute any and all of this and setup steps are included below.

## Setup and Installation

### Types of Insulter

There are two versions of The Trumpspearean Insulter: **periodic** and **streaming** versions.

#### Periodic

The Periodic Insulter periodically tweets messages to Trump regardless of what and when he posts. I've configured mine to send a tweet per hour, but this is a flexible value you can change.

This is the reccomended default setup that allows you to 'set it and forget it' so to speak.

#### Streaming

The Streaming Insulter tweets replies directly to Trump _as he sends tweets_. 

This is reccomemded for those who have a consistently internet-connected machine or can restart the bot in a terminal whenever they are connected. Keep in mind that when the connection is lost you will not continue to monitor and reply to Trump's tweets in real time.

### Requirements

This code is written in Python 2 and relys on the tweepy library
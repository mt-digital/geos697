# geos697
## Treasure Valley Final Project for GEOS 697 Summer EPSCoR Course

This project is the group efforts for the GEOS 697 intensive course on Interdisciplinary Modeling. We 
studied social, ecological, economic, and hydrological systems throughout. This project specifically was
generated and guided by Professor Lejo Flores at Boise State University.

### Install dependencies

#### 1. MongoDB

MongoDB is our database of choice for this project because we can easily create
key-value pairs (think Python dictionary) where the key is a set of parameters 
that feed into our model and the values are arrays, the model output for the 
chosen set of parameters.

##### OS X

On OS X, installing MongoDB is pretty straightforward if you have homebrew 
installed. If not, [get homebrew](http://brew.sh), you'll be glad you did 
since you'll have access to many great scientific and programming packages.

After you install Homebrew, install MongoDB:

```
brew install mongodb
```

When this finishes, it gives us two instructions to follow to start using 
MongoDB, 

```    
    To have launchd start mongodb at login:
        ln -sfv /usr/local/opt/mongodb/*.plist ~/Library/LaunchAgents
    Then to load mongodb now:
        launchctl load ~/Library/LaunchAgents/homebrew.mxcl.mongodb.plist
```

Follow these instructions, then type `mongo` at the command line. 
If you see a new prompt ending with `>` then MongoDB is installed and ready.

##### Linux

Follow the instructions: http://docs.mongodb.org/manual/administration/install-on-linux

##### Windows

I don't know. If you do it, please post it here.


#### 2. Set up and start the web server

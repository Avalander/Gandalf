# Gandalf

Gandalf is a script manager for Unix. It aims to provide a console interface to create and use scripts without polluting the `/usr/local/bin` folder.

In it's current state, it arguably doesn't provide any read advantage over simply dropping script files in `/usr/local/bin`, but it's a fun side project.

## Installation

There is currently no way to install Gandalf from any package manager or similar system. If you want to give it a try, however, you can always clone this reposiotry and create a symbolic link to `gandalf.py` in `/usr/local/bin` or any other folder included in your `PATH`.

## Usage

Gandalf provides five basic commands:
### Create
Creates a new script file.
```
$ gandalf create {script-name} [-d {description}] [-e {editor}]
```

- **script-name:** the name that will be used to invoke this script.
- **description:** an optional string that will be provided when listing the script.
- **editor:** an optional editor name that will be used when editing the script file. Default is `nano`.

### Edit
Updates an existing script.
```
$ gandalf edit {script-name} [-e {editor}]
```

- **script-name:** the name of the script that will be edited.
- **editor:** an optional editor name that will be used when editing the script file. Default is `nano`.

### List
Lists all existing scripts. If a description argument has been provided when creating a script, it will be listed next to its name.
```
$ gandalf list
```

### Remove
Removes and existing script.
```
$ gandalf remove {script-name}
```

- **script-name:** the name of the script that will be removed.

### Run
Executes a given script.
```
$ gandalf run {script-name} [-a {arguments}]
```

- **script-name:** the name of the script that will be executed.
- **arguments:** an optional list of arguments that will be provided to the script when invoked.

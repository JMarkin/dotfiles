complete -c rustic -n "__fish_use_subcommand" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_use_subcommand" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_use_subcommand" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_use_subcommand" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_use_subcommand" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_use_subcommand" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_use_subcommand" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_use_subcommand" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_use_subcommand" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_use_subcommand" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_use_subcommand" -s V -l version -d 'Print version information'
complete -c rustic -n "__fish_use_subcommand" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_use_subcommand" -f -a "backup" -d 'Backup to the repository'
complete -c rustic -n "__fish_use_subcommand" -f -a "cat" -d 'Show raw data of repository files and blobs'
complete -c rustic -n "__fish_use_subcommand" -f -a "config" -d 'Change the repository configuration'
complete -c rustic -n "__fish_use_subcommand" -f -a "completions" -d 'Generate shell completions'
complete -c rustic -n "__fish_use_subcommand" -f -a "check" -d 'Check the repository'
complete -c rustic -n "__fish_use_subcommand" -f -a "diff" -d 'Compare two snapshots/paths'
complete -c rustic -n "__fish_use_subcommand" -f -a "forget" -d 'Remove snapshots from the repository'
complete -c rustic -n "__fish_use_subcommand" -f -a "init" -d 'Initialize a new repository'
complete -c rustic -n "__fish_use_subcommand" -f -a "key" -d 'Manage keys'
complete -c rustic -n "__fish_use_subcommand" -f -a "list" -d 'List repository files'
complete -c rustic -n "__fish_use_subcommand" -f -a "ls" -d 'List file contents of a snapshot'
complete -c rustic -n "__fish_use_subcommand" -f -a "snapshots" -d 'Show a detailed overview of the snapshots within the repository'
complete -c rustic -n "__fish_use_subcommand" -f -a "self-update" -d 'Update to the latest rustic release'
complete -c rustic -n "__fish_use_subcommand" -f -a "prune" -d 'Remove unused data or repack repository pack files'
complete -c rustic -n "__fish_use_subcommand" -f -a "restore" -d 'Restore a snapshot/path'
complete -c rustic -n "__fish_use_subcommand" -f -a "repoinfo" -d 'Show general information about the repository'
complete -c rustic -n "__fish_use_subcommand" -f -a "tag" -d 'Change tags of snapshots'
complete -c rustic -n "__fish_use_subcommand" -f -a "help" -d 'Print this message or the help of the given subcommand(s)'
complete -c rustic -n "__fish_seen_subcommand_from backup" -l parent -d 'Snapshot to use as parent' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -l tag -d 'Tags to add to backup (can be specified multiple times)' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -l delete-after -d 'Mark snapshot to be deleted after given duration (e.g. 10d)' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -l stdin-filename -d 'Set filename to be used when backing up from stdin' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -l host -d 'Set the host name manually' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -s g -l glob -d 'Glob pattern to exclude/include (can be specified multiple times)' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -l iglob -d 'Same as --glob pattern but ignores the casing of filenames' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -l glob-file -d 'Read glob patterns to exclude/include from this file (can be specified multiple times)' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -l iglob-file -d 'Same as --glob-file ignores the casing of filenames in patterns' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -l exclude-if-present -d 'Exclude contents of directories containing this filename (can be specified multiple times)' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -l exclude-larger-than -d 'Maximum size of files to be backuped. Larger files will be excluded' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from backup" -s n -l dry-run -d 'Do not upload or write any data, just show what would be done'
complete -c rustic -n "__fish_seen_subcommand_from backup" -s f -l force -d 'Use no parent, read all files'
complete -c rustic -n "__fish_seen_subcommand_from backup" -l ignore-ctime -d 'Ignore ctime changes when checking for modified files'
complete -c rustic -n "__fish_seen_subcommand_from backup" -l ignore-inode -d 'Ignore inode number changes when checking for modified files'
complete -c rustic -n "__fish_seen_subcommand_from backup" -l delete-never -d 'Mark snapshot as uneraseable'
complete -c rustic -n "__fish_seen_subcommand_from backup" -l with-atime -d 'Save access time for files and directories'
complete -c rustic -n "__fish_seen_subcommand_from backup" -l git-ignore -d 'Ignore files based on .gitignore files'
complete -c rustic -n "__fish_seen_subcommand_from backup" -s x -l one-file-system -d 'Exclude other file systems, don\'t cross filesystem boundaries and subvolumes'
complete -c rustic -n "__fish_seen_subcommand_from backup" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from backup" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from cat; and not __fish_seen_subcommand_from tree-blob; and not __fish_seen_subcommand_from data-blob; and not __fish_seen_subcommand_from config; and not __fish_seen_subcommand_from index; and not __fish_seen_subcommand_from snapshot; and not __fish_seen_subcommand_from tree; and not __fish_seen_subcommand_from help" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and not __fish_seen_subcommand_from tree-blob; and not __fish_seen_subcommand_from data-blob; and not __fish_seen_subcommand_from config; and not __fish_seen_subcommand_from index; and not __fish_seen_subcommand_from snapshot; and not __fish_seen_subcommand_from tree; and not __fish_seen_subcommand_from help" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and not __fish_seen_subcommand_from tree-blob; and not __fish_seen_subcommand_from data-blob; and not __fish_seen_subcommand_from config; and not __fish_seen_subcommand_from index; and not __fish_seen_subcommand_from snapshot; and not __fish_seen_subcommand_from tree; and not __fish_seen_subcommand_from help" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and not __fish_seen_subcommand_from tree-blob; and not __fish_seen_subcommand_from data-blob; and not __fish_seen_subcommand_from config; and not __fish_seen_subcommand_from index; and not __fish_seen_subcommand_from snapshot; and not __fish_seen_subcommand_from tree; and not __fish_seen_subcommand_from help" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and not __fish_seen_subcommand_from tree-blob; and not __fish_seen_subcommand_from data-blob; and not __fish_seen_subcommand_from config; and not __fish_seen_subcommand_from index; and not __fish_seen_subcommand_from snapshot; and not __fish_seen_subcommand_from tree; and not __fish_seen_subcommand_from help" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and not __fish_seen_subcommand_from tree-blob; and not __fish_seen_subcommand_from data-blob; and not __fish_seen_subcommand_from config; and not __fish_seen_subcommand_from index; and not __fish_seen_subcommand_from snapshot; and not __fish_seen_subcommand_from tree; and not __fish_seen_subcommand_from help" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and not __fish_seen_subcommand_from tree-blob; and not __fish_seen_subcommand_from data-blob; and not __fish_seen_subcommand_from config; and not __fish_seen_subcommand_from index; and not __fish_seen_subcommand_from snapshot; and not __fish_seen_subcommand_from tree; and not __fish_seen_subcommand_from help" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and not __fish_seen_subcommand_from tree-blob; and not __fish_seen_subcommand_from data-blob; and not __fish_seen_subcommand_from config; and not __fish_seen_subcommand_from index; and not __fish_seen_subcommand_from snapshot; and not __fish_seen_subcommand_from tree; and not __fish_seen_subcommand_from help" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and not __fish_seen_subcommand_from tree-blob; and not __fish_seen_subcommand_from data-blob; and not __fish_seen_subcommand_from config; and not __fish_seen_subcommand_from index; and not __fish_seen_subcommand_from snapshot; and not __fish_seen_subcommand_from tree; and not __fish_seen_subcommand_from help" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and not __fish_seen_subcommand_from tree-blob; and not __fish_seen_subcommand_from data-blob; and not __fish_seen_subcommand_from config; and not __fish_seen_subcommand_from index; and not __fish_seen_subcommand_from snapshot; and not __fish_seen_subcommand_from tree; and not __fish_seen_subcommand_from help" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from cat; and not __fish_seen_subcommand_from tree-blob; and not __fish_seen_subcommand_from data-blob; and not __fish_seen_subcommand_from config; and not __fish_seen_subcommand_from index; and not __fish_seen_subcommand_from snapshot; and not __fish_seen_subcommand_from tree; and not __fish_seen_subcommand_from help" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from cat; and not __fish_seen_subcommand_from tree-blob; and not __fish_seen_subcommand_from data-blob; and not __fish_seen_subcommand_from config; and not __fish_seen_subcommand_from index; and not __fish_seen_subcommand_from snapshot; and not __fish_seen_subcommand_from tree; and not __fish_seen_subcommand_from help" -f -a "tree-blob" -d 'Display a tree blob'
complete -c rustic -n "__fish_seen_subcommand_from cat; and not __fish_seen_subcommand_from tree-blob; and not __fish_seen_subcommand_from data-blob; and not __fish_seen_subcommand_from config; and not __fish_seen_subcommand_from index; and not __fish_seen_subcommand_from snapshot; and not __fish_seen_subcommand_from tree; and not __fish_seen_subcommand_from help" -f -a "data-blob" -d 'Display a data blob'
complete -c rustic -n "__fish_seen_subcommand_from cat; and not __fish_seen_subcommand_from tree-blob; and not __fish_seen_subcommand_from data-blob; and not __fish_seen_subcommand_from config; and not __fish_seen_subcommand_from index; and not __fish_seen_subcommand_from snapshot; and not __fish_seen_subcommand_from tree; and not __fish_seen_subcommand_from help" -f -a "config" -d 'Display the config file'
complete -c rustic -n "__fish_seen_subcommand_from cat; and not __fish_seen_subcommand_from tree-blob; and not __fish_seen_subcommand_from data-blob; and not __fish_seen_subcommand_from config; and not __fish_seen_subcommand_from index; and not __fish_seen_subcommand_from snapshot; and not __fish_seen_subcommand_from tree; and not __fish_seen_subcommand_from help" -f -a "index" -d 'Display an index file'
complete -c rustic -n "__fish_seen_subcommand_from cat; and not __fish_seen_subcommand_from tree-blob; and not __fish_seen_subcommand_from data-blob; and not __fish_seen_subcommand_from config; and not __fish_seen_subcommand_from index; and not __fish_seen_subcommand_from snapshot; and not __fish_seen_subcommand_from tree; and not __fish_seen_subcommand_from help" -f -a "snapshot" -d 'Display a snapshot file'
complete -c rustic -n "__fish_seen_subcommand_from cat; and not __fish_seen_subcommand_from tree-blob; and not __fish_seen_subcommand_from data-blob; and not __fish_seen_subcommand_from config; and not __fish_seen_subcommand_from index; and not __fish_seen_subcommand_from snapshot; and not __fish_seen_subcommand_from tree; and not __fish_seen_subcommand_from help" -f -a "tree" -d 'Display a tree within a snapshot'
complete -c rustic -n "__fish_seen_subcommand_from cat; and not __fish_seen_subcommand_from tree-blob; and not __fish_seen_subcommand_from data-blob; and not __fish_seen_subcommand_from config; and not __fish_seen_subcommand_from index; and not __fish_seen_subcommand_from snapshot; and not __fish_seen_subcommand_from tree; and not __fish_seen_subcommand_from help" -f -a "help" -d 'Print this message or the help of the given subcommand(s)'
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree-blob" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree-blob" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree-blob" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree-blob" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree-blob" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree-blob" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree-blob" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree-blob" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree-blob" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree-blob" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree-blob" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from data-blob" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from data-blob" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from data-blob" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from data-blob" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from data-blob" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from data-blob" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from data-blob" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from data-blob" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from data-blob" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from data-blob" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from data-blob" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from config" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from config" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from config" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from config" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from config" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from config" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from config" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from config" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from config" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from config" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from config" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from index" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from index" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from index" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from index" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from index" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from index" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from index" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from index" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from index" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from index" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from index" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from snapshot" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from snapshot" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from snapshot" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from snapshot" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from snapshot" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from snapshot" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from snapshot" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from snapshot" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from snapshot" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from snapshot" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from snapshot" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from tree" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from help" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from help" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from help" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from help" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from help" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from help" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from help" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from help" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from help" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from cat; and __fish_seen_subcommand_from help" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from config" -l set-compression -d 'Set compression level. Allowed levels are 1 to 22 and -1 to -7, see https://facebook.github.io/zstd/. Note that 0 equals to no compression' -r
complete -c rustic -n "__fish_seen_subcommand_from config" -l set-version -d 'Set repository version. Allowed versions: 1,2' -r
complete -c rustic -n "__fish_seen_subcommand_from config" -l set-treepack-size -d 'Set default packsize for tree packs. rustic tries to always produce packs greater than this value. Note that for large repos, this value is grown by the grown factor. Defaults to 4 MiB if not set' -r
complete -c rustic -n "__fish_seen_subcommand_from config" -l set-treepack-size-limit -d 'Set upper limit for default packsize for tree packs. Note that packs actually can get up to some MiBs larger. If not set, pack sizes can grow up to approximately 4 GiB' -r
complete -c rustic -n "__fish_seen_subcommand_from config" -l set-treepack-growfactor -d 'Set grow factor for tree packs. The default packsize grows by the square root of the total size of all tree packs multiplied with this factor. This means 32 kiB times this factor per square root of total treesize in GiB. Defaults to 32 (= 1MB per sqare root of total treesize in GiB) if not set' -r
complete -c rustic -n "__fish_seen_subcommand_from config" -l set-datapack-size -d 'Set default packsize for data packs. rustic tries to always produce packs greater than this value. Note that for large repos, this value is grown by the grown factor. Defaults to 32 MiB if not set' -r
complete -c rustic -n "__fish_seen_subcommand_from config" -l set-datapack-growfactor -d 'Set grow factor for data packs. The default packsize grows by the square root of the total size of all data packs multiplied with this factor. This means 32 kiB times this factor per square root of total datasize in GiB. Defaults to 32 (= 1MB per sqare root of total datasize in GiB) if not set' -r
complete -c rustic -n "__fish_seen_subcommand_from config" -l set-datapack-size-limit -d 'Set upper limit for default packsize for tree packs. Note that packs actually can get up to some MiBs larger. If not set, pack sizes can grow up to approximately 4 GiB' -r
complete -c rustic -n "__fish_seen_subcommand_from config" -l set-min-packsize-tolerate-percent -d 'Set minimum tolerated packsize in percent of the targeted packsize. Defaults to 30 if not set' -r
complete -c rustic -n "__fish_seen_subcommand_from config" -l set-max-packsize-tolerate-percent -d 'Set maximum tolerated packsize in percent of the targeted packsize A value of 0 means packs larger than the targeted packsize are always tolerated. Default if not set: larger packfiles are always tolerated' -r
complete -c rustic -n "__fish_seen_subcommand_from config" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from config" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from config" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from config" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from config" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from config" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from config" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from config" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from config" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from config" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from config" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from completions" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from completions" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from completions" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from completions" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from completions" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from completions" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from completions" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from completions" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from completions" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from completions" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from completions" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from check" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from check" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from check" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from check" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from check" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from check" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from check" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from check" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from check" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from check" -l trust-cache -d 'Don\'t verify the data saved in the cache'
complete -c rustic -n "__fish_seen_subcommand_from check" -l read-data -d 'Read all data blobs'
complete -c rustic -n "__fish_seen_subcommand_from check" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from check" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from diff" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from diff" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from diff" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from diff" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from diff" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from diff" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from diff" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from diff" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from diff" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from diff" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from diff" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from forget" -s g -l group-by -d 'Group snapshots by any combination of host,paths,tags (default: "host,paths")' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l filter-paths -d 'Path list to filter (can be specified multiple times)' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l filter-tags -d 'Tag list to filter (can be specified multiple times)' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l filter-host -d 'Hostname to filter (can be specified multiple times)' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l keep-tags -d 'Keep snapshots with this taglist (can be specified multiple times)' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l keep-id -d 'Keep snapshots ids that start with ID (can be specified multiple times)' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -s l -l keep-last -d 'Keep the last N snapshots' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -s H -l keep-hourly -d 'Keep the last N hourly snapshots' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -s d -l keep-daily -d 'Keep the last N daily snapshots' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -s w -l keep-weekly -d 'Keep the last N weekly snapshots' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -s m -l keep-monthly -d 'Keep the last N monthly snapshots' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -s y -l keep-yearly -d 'Keep the last N yearly snapshots' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l keep-within -d 'Keep snapshots newer than DURATION relative to latest snapshot' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l keep-within-hourly -d 'Keep hourly snapshots newer than DURATION relative to latest snapshot' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l keep-within-daily -d 'Keep daily snapshots newer than DURATION relative to latest snapshot' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l keep-within-weekly -d 'Keep weekly snapshots newer than DURATION relative to latest snapshot' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l keep-within-monthly -d 'Keep monthly snapshots newer than DURATION relative to latest snapshot' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l keep-within-yearly -d 'Keep yearly snapshots newer than DURATION relative to latest snapshot' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l max-repack -d 'Define maximum data to repack in % of reposize or as size (e.g. \'5b\', \'2 kB\', \'3M\', \'4TiB\') or \'unlimited\'' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l max-unused -d 'Tolerate limit of unused data in % of reposize after pruning or as size (e.g. \'5b\', \'2 kB\', \'3M\', \'4TiB\') or \'unlimited\'' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l keep-pack -d 'Minimum duration (e.g. 90d) to keep packs before repacking or removing. More recently created packs won\'t be repacked or marked for deletion within this prune run' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l keep-delete -d 'Minimum duration (e.g. 10m) to keep packs marked for deletion. More recently marked packs won\'t be deleted within this prune run' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l repack-cacheable-only -d 'Only repack packs which are cacheable [default: true for a hot/cold repository, else false]' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l warm-up-command -d 'Warm up needed data pack files by running the command with %id replaced by pack id' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l warm-up-wait -d 'Duration (e.g. 10m) to wait after warm up before doing the actual restore' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from forget" -l prune -d 'Also prune the repository'
complete -c rustic -n "__fish_seen_subcommand_from forget" -s n -l dry-run -d 'Don\'t remove anything, only show what would be done'
complete -c rustic -n "__fish_seen_subcommand_from forget" -l instant-delete -d 'Delete files immediately instead of marking them. This also removes all files already marked for deletion. WARNING: Only use if you are sure the repository is not accessed by parallel processes!'
complete -c rustic -n "__fish_seen_subcommand_from forget" -l cache-only -d 'Only remove unneded pack file from local cache. Do not change the repository at all'
complete -c rustic -n "__fish_seen_subcommand_from forget" -l fast-repack -d 'Simply copy blobs when repacking instead of decrypting; possibly compressing; encrypting'
complete -c rustic -n "__fish_seen_subcommand_from forget" -l repack-uncompressed -d 'Repack packs containing uncompressed blobs. This cannot be used with --fast-repack. Implies --max-unused=0'
complete -c rustic -n "__fish_seen_subcommand_from forget" -l no-resize -d 'Do not repack packs which only needs to be resized'
complete -c rustic -n "__fish_seen_subcommand_from forget" -l warm-up -d 'Warm up needed data pack files by only requesting them without processing'
complete -c rustic -n "__fish_seen_subcommand_from forget" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from forget" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from init" -l hostname -d 'Set \'hostname\' in public key information' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -l username -d 'Set \'username\' in public key information' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -l set-compression -d 'Set compression level. Allowed levels are 1 to 22 and -1 to -7, see https://facebook.github.io/zstd/. Note that 0 equals to no compression' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -l set-version -d 'Set repository version. Allowed versions: 1,2' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -l set-treepack-size -d 'Set default packsize for tree packs. rustic tries to always produce packs greater than this value. Note that for large repos, this value is grown by the grown factor. Defaults to 4 MiB if not set' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -l set-treepack-size-limit -d 'Set upper limit for default packsize for tree packs. Note that packs actually can get up to some MiBs larger. If not set, pack sizes can grow up to approximately 4 GiB' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -l set-treepack-growfactor -d 'Set grow factor for tree packs. The default packsize grows by the square root of the total size of all tree packs multiplied with this factor. This means 32 kiB times this factor per square root of total treesize in GiB. Defaults to 32 (= 1MB per sqare root of total treesize in GiB) if not set' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -l set-datapack-size -d 'Set default packsize for data packs. rustic tries to always produce packs greater than this value. Note that for large repos, this value is grown by the grown factor. Defaults to 32 MiB if not set' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -l set-datapack-growfactor -d 'Set grow factor for data packs. The default packsize grows by the square root of the total size of all data packs multiplied with this factor. This means 32 kiB times this factor per square root of total datasize in GiB. Defaults to 32 (= 1MB per sqare root of total datasize in GiB) if not set' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -l set-datapack-size-limit -d 'Set upper limit for default packsize for tree packs. Note that packs actually can get up to some MiBs larger. If not set, pack sizes can grow up to approximately 4 GiB' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -l set-min-packsize-tolerate-percent -d 'Set minimum tolerated packsize in percent of the targeted packsize. Defaults to 30 if not set' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -l set-max-packsize-tolerate-percent -d 'Set maximum tolerated packsize in percent of the targeted packsize A value of 0 means packs larger than the targeted packsize are always tolerated. Default if not set: larger packfiles are always tolerated' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from init" -l with-created -d 'Add \'created\' date in public key information'
complete -c rustic -n "__fish_seen_subcommand_from init" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from init" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from key; and not __fish_seen_subcommand_from add; and not __fish_seen_subcommand_from help" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and not __fish_seen_subcommand_from add; and not __fish_seen_subcommand_from help" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and not __fish_seen_subcommand_from add; and not __fish_seen_subcommand_from help" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and not __fish_seen_subcommand_from add; and not __fish_seen_subcommand_from help" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and not __fish_seen_subcommand_from add; and not __fish_seen_subcommand_from help" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and not __fish_seen_subcommand_from add; and not __fish_seen_subcommand_from help" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and not __fish_seen_subcommand_from add; and not __fish_seen_subcommand_from help" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and not __fish_seen_subcommand_from add; and not __fish_seen_subcommand_from help" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and not __fish_seen_subcommand_from add; and not __fish_seen_subcommand_from help" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and not __fish_seen_subcommand_from add; and not __fish_seen_subcommand_from help" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from key; and not __fish_seen_subcommand_from add; and not __fish_seen_subcommand_from help" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from key; and not __fish_seen_subcommand_from add; and not __fish_seen_subcommand_from help" -f -a "add"
complete -c rustic -n "__fish_seen_subcommand_from key; and not __fish_seen_subcommand_from add; and not __fish_seen_subcommand_from help" -f -a "help" -d 'Print this message or the help of the given subcommand(s)'
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from add" -l new-password-file -d 'File from which to read the new password' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from add" -l hostname -d 'Set \'hostname\' in public key information' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from add" -l username -d 'Set \'username\' in public key information' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from add" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from add" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from add" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from add" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from add" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from add" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from add" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from add" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from add" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from add" -l with-created -d 'Add \'created\' date in public key information'
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from add" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from add" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from help" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from help" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from help" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from help" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from help" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from help" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from help" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from help" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from help" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from key; and __fish_seen_subcommand_from help" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from list" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from list" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from list" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from list" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from list" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from list" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from list" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from list" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from list" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from list" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from list" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from ls" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from ls" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from ls" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from ls" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from ls" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from ls" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from ls" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from ls" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from ls" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from ls" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from ls" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from snapshots" -l filter-paths -d 'Path list to filter (can be specified multiple times)' -r
complete -c rustic -n "__fish_seen_subcommand_from snapshots" -l filter-tags -d 'Tag list to filter (can be specified multiple times)' -r
complete -c rustic -n "__fish_seen_subcommand_from snapshots" -l filter-host -d 'Hostname to filter (can be specified multiple times)' -r
complete -c rustic -n "__fish_seen_subcommand_from snapshots" -s g -l group-by -d 'Group snapshots by any combination of host,paths,tags' -r
complete -c rustic -n "__fish_seen_subcommand_from snapshots" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from snapshots" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from snapshots" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from snapshots" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from snapshots" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from snapshots" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from snapshots" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from snapshots" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from snapshots" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from snapshots" -l long -d 'Show detailed information about snapshots'
complete -c rustic -n "__fish_seen_subcommand_from snapshots" -l json -d 'Show snapshots in json format'
complete -c rustic -n "__fish_seen_subcommand_from snapshots" -l all -d 'Show all snapshots instead of summarizing identical follow-up snapshots'
complete -c rustic -n "__fish_seen_subcommand_from snapshots" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from snapshots" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from self-update" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from self-update" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from self-update" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from self-update" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from self-update" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from self-update" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from self-update" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from self-update" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from self-update" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from self-update" -l force -d 'Do not ask before processing the self-update'
complete -c rustic -n "__fish_seen_subcommand_from self-update" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from self-update" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from prune" -l max-repack -d 'Define maximum data to repack in % of reposize or as size (e.g. \'5b\', \'2 kB\', \'3M\', \'4TiB\') or \'unlimited\'' -r
complete -c rustic -n "__fish_seen_subcommand_from prune" -l max-unused -d 'Tolerate limit of unused data in % of reposize after pruning or as size (e.g. \'5b\', \'2 kB\', \'3M\', \'4TiB\') or \'unlimited\'' -r
complete -c rustic -n "__fish_seen_subcommand_from prune" -l keep-pack -d 'Minimum duration (e.g. 90d) to keep packs before repacking or removing. More recently created packs won\'t be repacked or marked for deletion within this prune run' -r
complete -c rustic -n "__fish_seen_subcommand_from prune" -l keep-delete -d 'Minimum duration (e.g. 10m) to keep packs marked for deletion. More recently marked packs won\'t be deleted within this prune run' -r
complete -c rustic -n "__fish_seen_subcommand_from prune" -l repack-cacheable-only -d 'Only repack packs which are cacheable [default: true for a hot/cold repository, else false]' -r
complete -c rustic -n "__fish_seen_subcommand_from prune" -l warm-up-command -d 'Warm up needed data pack files by running the command with %id replaced by pack id' -r
complete -c rustic -n "__fish_seen_subcommand_from prune" -l warm-up-wait -d 'Duration (e.g. 10m) to wait after warm up before doing the actual restore' -r
complete -c rustic -n "__fish_seen_subcommand_from prune" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from prune" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from prune" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from prune" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from prune" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from prune" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from prune" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from prune" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from prune" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from prune" -s n -l dry-run -d 'Don\'t remove anything, only show what would be done'
complete -c rustic -n "__fish_seen_subcommand_from prune" -l instant-delete -d 'Delete files immediately instead of marking them. This also removes all files already marked for deletion. WARNING: Only use if you are sure the repository is not accessed by parallel processes!'
complete -c rustic -n "__fish_seen_subcommand_from prune" -l cache-only -d 'Only remove unneded pack file from local cache. Do not change the repository at all'
complete -c rustic -n "__fish_seen_subcommand_from prune" -l fast-repack -d 'Simply copy blobs when repacking instead of decrypting; possibly compressing; encrypting'
complete -c rustic -n "__fish_seen_subcommand_from prune" -l repack-uncompressed -d 'Repack packs containing uncompressed blobs. This cannot be used with --fast-repack. Implies --max-unused=0'
complete -c rustic -n "__fish_seen_subcommand_from prune" -l no-resize -d 'Do not repack packs which only needs to be resized'
complete -c rustic -n "__fish_seen_subcommand_from prune" -l warm-up -d 'Warm up needed data pack files by only requesting them without processing'
complete -c rustic -n "__fish_seen_subcommand_from prune" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from prune" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from restore" -l warm-up-command -d 'Warm up needed data pack files by running the command with %id replaced by pack id' -r
complete -c rustic -n "__fish_seen_subcommand_from restore" -l warm-up-wait -d 'Duration (e.g. 10m) to wait after warm up before doing the actual restore' -r
complete -c rustic -n "__fish_seen_subcommand_from restore" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from restore" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from restore" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from restore" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from restore" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from restore" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from restore" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from restore" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from restore" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from restore" -s n -l dry-run -d 'Dry-run: don\'t restore, only show what would be done'
complete -c rustic -n "__fish_seen_subcommand_from restore" -l delete -d 'Remove all files/dirs in destination which are not contained in snapshot. WARNING: Use with care, maybe first try this first with --dry-run?'
complete -c rustic -n "__fish_seen_subcommand_from restore" -l numeric-id -d 'Use numeric ids instead of user/group when restoring uid/gui'
complete -c rustic -n "__fish_seen_subcommand_from restore" -l warm-up -d 'Warm up needed data pack files by only requesting them without processing'
complete -c rustic -n "__fish_seen_subcommand_from restore" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from restore" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from repoinfo" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from repoinfo" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from repoinfo" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from repoinfo" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from repoinfo" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from repoinfo" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from repoinfo" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from repoinfo" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from repoinfo" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from repoinfo" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from repoinfo" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from tag" -l filter-paths -d 'Path list to filter (can be specified multiple times)' -r
complete -c rustic -n "__fish_seen_subcommand_from tag" -l filter-tags -d 'Tag list to filter (can be specified multiple times)' -r
complete -c rustic -n "__fish_seen_subcommand_from tag" -l filter-host -d 'Hostname to filter (can be specified multiple times)' -r
complete -c rustic -n "__fish_seen_subcommand_from tag" -l add -d 'Tags to add (can be specified multiple times)' -r
complete -c rustic -n "__fish_seen_subcommand_from tag" -l remove -d 'Tags to remove (can be specified multiple times)' -r
complete -c rustic -n "__fish_seen_subcommand_from tag" -l set -d 'Tag list to set (can be specified multiple times)' -r
complete -c rustic -n "__fish_seen_subcommand_from tag" -l set-delete-after -d 'Mark snapshot to be deleted after given duration (e.g. 10d)' -r
complete -c rustic -n "__fish_seen_subcommand_from tag" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from tag" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from tag" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from tag" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from tag" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from tag" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from tag" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from tag" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from tag" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from tag" -s n -l dry-run -d 'Don\'t change any snapshot, only show which would be modified'
complete -c rustic -n "__fish_seen_subcommand_from tag" -l remove-delete -d 'Remove any delete mark'
complete -c rustic -n "__fish_seen_subcommand_from tag" -l set-delete-never -d 'Mark snapshot as uneraseable'
complete -c rustic -n "__fish_seen_subcommand_from tag" -s h -l help -d 'Print help information'
complete -c rustic -n "__fish_seen_subcommand_from tag" -l no-cache -d 'Don\'t use a cache'
complete -c rustic -n "__fish_seen_subcommand_from help" -s r -l repository -d 'Repository to use' -r
complete -c rustic -n "__fish_seen_subcommand_from help" -l repo-hot -d 'Repository to use as hot storage' -r
complete -c rustic -n "__fish_seen_subcommand_from help" -l password -d 'Password of the repository - WARNING: Using --password can reveal the password in the process list!' -r
complete -c rustic -n "__fish_seen_subcommand_from help" -s p -l password-file -d 'File to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from help" -l password-command -d 'Command to read the password from' -r
complete -c rustic -n "__fish_seen_subcommand_from help" -l log-level -d 'Use this log level [default: info]' -r
complete -c rustic -n "__fish_seen_subcommand_from help" -l log-file -d 'Write log messages to the given file instead of printing them. Note: warnings and errors are still additionally printed unless they are ignored by --log-level' -r
complete -c rustic -n "__fish_seen_subcommand_from help" -l cache-dir -d 'Use this dir as cache dir instead of the standard cache dir' -r
complete -c rustic -n "__fish_seen_subcommand_from help" -s P -l config-profile -d 'Config profile to use. This parses the file <PROFILE>.toml in the config directory' -r
complete -c rustic -n "__fish_seen_subcommand_from help" -l no-cache -d 'Don\'t use a cache'

# disable checks
self: super: {

  ruff = super.ruff.overrideAttrs {
    checkFlags = super.lib.optionals super.stdenv.hostPlatform.isDarwin [
      # "--skip=add_search_path"
      # "--skip=changed_file"
      # "--skip=changed_versions_file"
      # "--skip=deleted_file"
      # "--skip=directory_deleted"
      # "--skip=directory_moved_to_trash"
      # "--skip=directory_moved_to_workspace"
      # "--skip=directory_renamed"
      # "--skip=hard_links_in_workspace"
      # "--skip=hard_links_to_target_outside_workspace"
      # "--skip=move_file_to_trash"
      # "--skip=move_file_to_workspace"
      # "--skip=nested_packages_delete_root"
      # "--skip=new_file"
      # "--skip=new_ignored_file"
      # "--skip=removed_package"
      # "--skip=rename_file"
      # "--skip=search_path"
      # "--skip=unix::changed_metadata"
      # "--skip=unix::symlinked_module_search_path"
      # "--skip=unix::symlink_inside_workspace"
    ];
  };
}

{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
	nativeBuildInputs = with pkgs; [
		python310Packages.forbiddenfruit
	];
}

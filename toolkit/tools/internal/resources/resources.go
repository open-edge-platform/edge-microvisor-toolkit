// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

package resources

import (
	"embed"
)

const (
	AssetsGrubCfgFile      = "assets/grub2/grub.cfg"
	AssetsGrubDefFile      = "assets/grub2/grub"
	AssetsBootParmsDefFile = "assets/efi/bootParms.conf"
)

//go:embed assets
var ResourcesFS embed.FS

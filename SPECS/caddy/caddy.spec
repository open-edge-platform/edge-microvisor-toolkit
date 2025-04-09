%global goipath github.com/caddyserver/caddy

Summary:        Web server with automatic HTTPS
Name:           caddy
Version:        2.9.1
Release:        10%{?dist}
Distribution:   Edge Microvisor Toolkit
Vendor:         Intel Corporation
# main source code is Apache-2.0
# see comments above provides tags for bundled license breakdown
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT AND BSD-2-Clause-Views AND CC0-1.0 AND ISC AND MPL-2.0
URL:            https://caddyserver.com
Source0:        https://%{goipath}/archive/v%{version}/caddy-%{version}.tar.gz

# vendored dependencies
Source1:        caddy-%{version}-vendor.tar.gz
Source2:        create-vendor-tarball.sh
Source3:        post-caddy.sh

# based on reference files upstream
# https://github.com/caddyserver/dist
Source10:       Caddyfile
Source20:       caddy.service
Source21:       caddy-api.service
Source22:       caddy.sysusers
Source30:       poweredby-white.png
Source31:       poweredby-black.png

# downstream only patch to disable commands that can alter the binary
Patch1:         0001-Disable-commands-that-can-alter-the-binary.patch
Patch2:         CVE-2025-22869.patch
Patch3:         CVE-2024-45339.patch
BuildRequires:  go-rpm-macros
# https://github.com/caddyserver/caddy/commit/2028da4e74cd41f0f7f94222c6599da1a371d4b8
BuildRequires:  golang >= 1.22.3
# dario.cat/mergo : BSD-3-Clause
Provides:       bundled(golang(dario.cat/mergo)) = 1.0.1
# filippo.io/edwards25519 : BSD-3-Clause
Provides:       bundled(golang(filippo.io/edwards25519)) = 1.1.0
# github.com/AndreasBriese/bbloom : MIT AND CC0-1.0
Provides:       bundled(golang(github.com/AndreasBriese/bbloom)) = 46b345b
# github.com/BurntSushi/toml : MIT
Provides:       bundled(golang(github.com/BurntSushi/toml)) = 1.4.0
# github.com/Masterminds/goutils : Apache-2.0
Provides:       bundled(golang(github.com/Masterminds/goutils)) = 1.1.1
# github.com/Masterminds/semver/v3 : MIT
Provides:       bundled(golang(github.com/Masterminds/semver/v3)) = 3.3.0
# github.com/Masterminds/sprig/v3 : MIT
Provides:       bundled(golang(github.com/Masterminds/sprig/v3)) = 3.3.0
# github.com/Microsoft/go-winio : MIT
Provides:       bundled(golang(github.com/Microsoft/go-winio)) = 0.6.0
# github.com/alecthomas/chroma/v2 : MIT
Provides:       bundled(golang(github.com/alecthomas/chroma/v2)) = 2.14.0
# github.com/antlr4-go/antlr/v4 : BSD-3-Clause
Provides:       bundled(golang(github.com/antlr4-go/antlr/v4)) = 4.13.0
# github.com/aryann/difflib : MIT
Provides:       bundled(golang(github.com/aryann/difflib)) = ff5ff6d
# github.com/beorn7/perks : MIT
Provides:       bundled(golang(github.com/beorn7/perks)) = 1.0.1
# github.com/caddyserver/certmagic : Apache-2.0
Provides:       bundled(golang(github.com/caddyserver/certmagic)) = 0.21.6
# github.com/caddyserver/zerossl : MIT
Provides:       bundled(golang(github.com/caddyserver/zerossl)) = 0.1.3
# github.com/cenkalti/backoff/v4 : MIT
Provides:       bundled(golang(github.com/cenkalti/backoff/v4)) = 4.3.0
# github.com/cespare/xxhash : MIT
Provides:       bundled(golang(github.com/cespare/xxhash)) = 1.1.0
# github.com/cespare/xxhash/v2 : MIT
Provides:       bundled(golang(github.com/cespare/xxhash/v2)) = 2.3.0
# github.com/chzyer/readline : MIT
Provides:       bundled(golang(github.com/chzyer/readline)) = 1.5.1
# github.com/cpuguy83/go-md2man/v2 : MIT
Provides:       bundled(golang(github.com/cpuguy83/go-md2man/v2)) = 2.0.4
# github.com/davecgh/go-spew : ISC
Provides:       bundled(golang(github.com/davecgh/go-spew)) = 1.1.1
# github.com/dgraph-io/badger : Apache-2.0
Provides:       bundled(golang(github.com/dgraph-io/badger)) = 1.6.2
# github.com/dgraph-io/badger/v2 : Apache-2.0
Provides:       bundled(golang(github.com/dgraph-io/badger/v2)) = 2.2007.4
# github.com/dgraph-io/ristretto : Apache-2.0 AND MIT
Provides:       bundled(golang(github.com/dgraph-io/ristretto)) = 0.1.0
# github.com/dgryski/go-farm : MIT
Provides:       bundled(golang(github.com/dgryski/go-farm)) = a6ae236
# github.com/dlclark/regexp2 : MIT
Provides:       bundled(golang(github.com/dlclark/regexp2)) = 1.11.0
# github.com/dustin/go-humanize : MIT
Provides:       bundled(golang(github.com/dustin/go-humanize)) = 1.0.1
# github.com/felixge/httpsnoop : MIT
Provides:       bundled(golang(github.com/felixge/httpsnoop)) = 1.0.4
# github.com/francoispqt/gojay : MIT
Provides:       bundled(golang(github.com/francoispqt/gojay)) = 1.2.13
# github.com/fxamacker/cbor/v2 : MIT
Provides:       bundled(golang(github.com/fxamacker/cbor/v2)) = 2.6.0
# github.com/go-chi/chi/v5 : MIT
Provides:       bundled(golang(github.com/go-chi/chi/v5)) = 5.0.12
# github.com/go-jose/go-jose/v3 : Apache-2.0 AND BSD-3-Clause
Provides:       bundled(golang(github.com/go-jose/go-jose/v3)) = 3.0.3
# github.com/go-kit/kit : MIT
Provides:       bundled(golang(github.com/go-kit/kit)) = 0.13.0
# github.com/go-kit/log : MIT
Provides:       bundled(golang(github.com/go-kit/log)) = 0.2.1
# github.com/go-logfmt/logfmt : MIT
Provides:       bundled(golang(github.com/go-logfmt/logfmt)) = 0.6.0
# github.com/go-logr/logr : Apache-2.0
Provides:       bundled(golang(github.com/go-logr/logr)) = 1.4.2
# github.com/go-logr/stdr : Apache-2.0
Provides:       bundled(golang(github.com/go-logr/stdr)) = 1.2.2
# github.com/go-sql-driver/mysql : MPL-2.0
Provides:       bundled(golang(github.com/go-sql-driver/mysql)) = 1.7.1
# github.com/go-task/slim-sprig : MIT
Provides:       bundled(golang(github.com/go-task/slim-sprig)) = 52ccab3
# github.com/golang/glog : Apache-2.0
Provides:       bundled(golang(github.com/golang/glog)) = 1.2.2
# github.com/golang/protobuf : BSD-3-Clause
Provides:       bundled(golang(github.com/golang/protobuf)) = 1.5.4
# github.com/golang/snappy : BSD-3-Clause
Provides:       bundled(golang(github.com/golang/snappy)) = 0.0.4
# github.com/google/cel-go : Apache-2.0
Provides:       bundled(golang(github.com/google/cel-go)) = 0.21.0
# github.com/google/certificate-transparency-go : Apache-2.0
Provides:       bundled(golang(github.com/google/certificate-transparency-go)) = 74a5dd3
# github.com/google/go-tpm : Apache-2.0
Provides:       bundled(golang(github.com/google/go-tpm)) = 0.9.0
# github.com/google/go-tspi : Apache-2.0
Provides:       bundled(golang(github.com/google/go-tspi)) = 0.3.0
# github.com/google/pprof : Apache-2.0
Provides:       bundled(golang(github.com/google/pprof)) = ec68065
# github.com/google/uuid : BSD-3-Clause
Provides:       bundled(golang(github.com/google/uuid)) = 1.6.0
# github.com/grpc-ecosystem/grpc-gateway/v2 : BSD-3-Clause
Provides:       bundled(golang(github.com/grpc-ecosystem/grpc-gateway/v2)) = 2.22.0
# github.com/huandu/xstrings : MIT
Provides:       bundled(golang(github.com/huandu/xstrings)) = 1.5.0
# github.com/inconshreveable/mousetrap : Apache-2.0
Provides:       bundled(golang(github.com/inconshreveable/mousetrap)) = 1.1.0
# github.com/jackc/chunkreader/v2 : MIT
Provides:       bundled(golang(github.com/jackc/chunkreader/v2)) = 2.0.1
# github.com/jackc/pgconn : MIT
Provides:       bundled(golang(github.com/jackc/pgconn)) = 1.14.3
# github.com/jackc/pgio : MIT
Provides:       bundled(golang(github.com/jackc/pgio)) = 1.0.0
# github.com/jackc/pgpassfile : MIT
Provides:       bundled(golang(github.com/jackc/pgpassfile)) = 1.0.0
# github.com/jackc/pgproto3/v2 : MIT
Provides:       bundled(golang(github.com/jackc/pgproto3/v2)) = 2.3.3
# github.com/jackc/pgservicefile : MIT
Provides:       bundled(golang(github.com/jackc/pgservicefile)) = 091c0ba
# github.com/jackc/pgtype : MIT
Provides:       bundled(golang(github.com/jackc/pgtype)) = 1.14.0
# github.com/jackc/pgx/v4 : MIT
Provides:       bundled(golang(github.com/jackc/pgx/v4)) = 4.18.3
# github.com/klauspost/compress : BSD-3-Clause AND Apache-2.0 AND MIT
Provides:       bundled(golang(github.com/klauspost/compress)) = 1.17.11
# github.com/klauspost/cpuid/v2 : MIT
Provides:       bundled(golang(github.com/klauspost/cpuid/v2)) = 2.2.9
# github.com/libdns/libdns : MIT
Provides:       bundled(golang(github.com/libdns/libdns)) = 0.2.2
# github.com/manifoldco/promptui : BSD-3-Clause
Provides:       bundled(golang(github.com/manifoldco/promptui)) = 0.9.0
# github.com/mattn/go-colorable : MIT
Provides:       bundled(golang(github.com/mattn/go-colorable)) = 0.1.13
# github.com/mattn/go-isatty : MIT
Provides:       bundled(golang(github.com/mattn/go-isatty)) = 0.0.20
# github.com/mgutz/ansi : MIT
Provides:       bundled(golang(github.com/mgutz/ansi)) = d51e80e
# github.com/mholt/acmez/v3 : Apache-2.0 AND BSD-3-Clause
Provides:       bundled(golang(github.com/mholt/acmez/v3)) = 3.0.0
# github.com/miekg/dns : BSD-3-Clause
Provides:       bundled(golang(github.com/miekg/dns)) = 1.1.62
# github.com/mitchellh/copystructure : MIT
Provides:       bundled(golang(github.com/mitchellh/copystructure)) = 1.2.0
# github.com/mitchellh/go-ps : MIT
Provides:       bundled(golang(github.com/mitchellh/go-ps)) = 1.0.0
# github.com/mitchellh/reflectwalk : MIT
Provides:       bundled(golang(github.com/mitchellh/reflectwalk)) = 1.0.2
# github.com/onsi/ginkgo/v2 : MIT
Provides:       bundled(golang(github.com/onsi/ginkgo/v2)) = 2.13.2
# github.com/pires/go-proxyproto : Apache-2.0
Provides:       bundled(golang(github.com/pires/go-proxyproto)) = b718e7c
# github.com/pkg/errors : BSD-2-Clause
Provides:       bundled(golang(github.com/pkg/errors)) = 0.9.1
# github.com/pmezard/go-difflib : BSD-3-Clause
Provides:       bundled(golang(github.com/pmezard/go-difflib)) = 1.0.0
# github.com/prometheus/client_golang : Apache-2.0
Provides:       bundled(golang(github.com/prometheus/client_golang)) = 1.19.1
# github.com/prometheus/client_model : Apache-2.0
Provides:       bundled(golang(github.com/prometheus/client_model)) = 0.5.0
# github.com/prometheus/common : Apache-2.0
Provides:       bundled(golang(github.com/prometheus/common)) = 0.48.0
# github.com/prometheus/procfs : Apache-2.0
Provides:       bundled(golang(github.com/prometheus/procfs)) = 0.12.0
# github.com/quic-go/qpack : MIT
Provides:       bundled(golang(github.com/quic-go/qpack)) = 0.5.1
# github.com/quic-go/quic-go : MIT
Provides:       bundled(golang(github.com/quic-go/quic-go)) = 0.48.2
# github.com/rs/xid : MIT
Provides:       bundled(golang(github.com/rs/xid)) = 1.5.0
# github.com/russross/blackfriday/v2 : BSD-2-Clause
Provides:       bundled(golang(github.com/russross/blackfriday/v2)) = 2.1.0
# github.com/shopspring/decimal : MIT
Provides:       bundled(golang(github.com/shopspring/decimal)) = 1.4.0
# github.com/shurcooL/sanitized_anchor_name : MIT
Provides:       bundled(golang(github.com/shurcooL/sanitized_anchor_name)) = 1.0.0
# github.com/sirupsen/logrus : MIT
Provides:       bundled(golang(github.com/sirupsen/logrus)) = 1.9.3
# github.com/slackhq/nebula : MIT
Provides:       bundled(golang(github.com/slackhq/nebula)) = 1.6.1
# github.com/smallstep/certificates : Apache-2.0
Provides:       bundled(golang(github.com/smallstep/certificates)) = 0.26.1
# github.com/smallstep/go-attestation : Apache-2.0
Provides:       bundled(golang(github.com/smallstep/go-attestation)) = 413678f
# github.com/smallstep/nosql : Apache-2.0
Provides:       bundled(golang(github.com/smallstep/nosql)) = 0.6.1
# github.com/smallstep/pkcs7 : MIT
Provides:       bundled(golang(github.com/smallstep/pkcs7)) = 3b98ecc
# github.com/smallstep/scep : MIT
Provides:       bundled(golang(github.com/smallstep/scep)) = aee96d7
# github.com/smallstep/truststore : Apache-2.0
Provides:       bundled(golang(github.com/smallstep/truststore)) = 0.13.0
# github.com/spf13/cast : MIT
Provides:       bundled(golang(github.com/spf13/cast)) = 1.7.0
# github.com/spf13/cobra : Apache-2.0
Provides:       bundled(golang(github.com/spf13/cobra)) = 1.8.1
# github.com/spf13/pflag : BSD-3-Clause
Provides:       bundled(golang(github.com/spf13/pflag)) = 1.0.5
# github.com/stoewer/go-strcase : MIT
Provides:       bundled(golang(github.com/stoewer/go-strcase)) = 1.2.0
# github.com/stretchr/testify : MIT
Provides:       bundled(golang(github.com/stretchr/testify)) = 1.9.0
# github.com/tailscale/tscert : BSD-3-Clause
Provides:       bundled(golang(github.com/tailscale/tscert)) = d3f8340
# github.com/urfave/cli : MIT
Provides:       bundled(golang(github.com/urfave/cli)) = 1.22.14
# github.com/x448/float16 : MIT
Provides:       bundled(golang(github.com/x448/float16)) = 0.8.4
# github.com/yuin/goldmark : MIT
Provides:       bundled(golang(github.com/yuin/goldmark)) = 1.7.8
# github.com/yuin/goldmark-highlighting/v2 : MIT
Provides:       bundled(golang(github.com/yuin/goldmark-highlighting/v2)) = 37449ab
# github.com/zeebo/blake3 : CC0-1.0
Provides:       bundled(golang(github.com/zeebo/blake3)) = 0.2.4
# go.etcd.io/bbolt : MIT
Provides:       bundled(golang(go.etcd.io/bbolt)) = 1.3.9
# go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp : Apache-2.0
Provides:       bundled(golang(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)) = 0.56.0
# go.opentelemetry.io/contrib/propagators/autoprop : Apache-2.0
Provides:       bundled(golang(go.opentelemetry.io/contrib/propagators/autoprop)) = 0.42.0
# go.opentelemetry.io/contrib/propagators/aws : Apache-2.0
Provides:       bundled(golang(go.opentelemetry.io/contrib/propagators/aws)) = 1.17.0
# go.opentelemetry.io/contrib/propagators/b3 : Apache-2.0
Provides:       bundled(golang(go.opentelemetry.io/contrib/propagators/b3)) = 1.17.0
# go.opentelemetry.io/contrib/propagators/jaeger : Apache-2.0
Provides:       bundled(golang(go.opentelemetry.io/contrib/propagators/jaeger)) = 1.17.0
# go.opentelemetry.io/contrib/propagators/ot : Apache-2.0
Provides:       bundled(golang(go.opentelemetry.io/contrib/propagators/ot)) = 1.17.0
# go.opentelemetry.io/otel : Apache-2.0
Provides:       bundled(golang(go.opentelemetry.io/otel)) = 1.31.0
# go.opentelemetry.io/otel/exporters/otlp/otlptrace : Apache-2.0
Provides:       bundled(golang(go.opentelemetry.io/otel/exporters/otlp/otlptrace)) = 1.31.0
# go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc : Apache-2.0
Provides:       bundled(golang(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)) = 1.31.0
# go.opentelemetry.io/otel/metric : Apache-2.0
Provides:       bundled(golang(go.opentelemetry.io/otel/metric)) = 1.31.0
# go.opentelemetry.io/otel/sdk : Apache-2.0
Provides:       bundled(golang(go.opentelemetry.io/otel/sdk)) = 1.31.0
# go.opentelemetry.io/otel/trace : Apache-2.0
Provides:       bundled(golang(go.opentelemetry.io/otel/trace)) = 1.31.0
# go.opentelemetry.io/proto/otlp : Apache-2.0
Provides:       bundled(golang(go.opentelemetry.io/proto/otlp)) = 1.3.1
# go.step.sm/cli-utils : Apache-2.0 AND BSD-2-Clause
Provides:       bundled(golang(go.step.sm/cli-utils)) = 0.9.0
# go.step.sm/crypto : Apache-2.0 AND BSD-2-Clause
Provides:       bundled(golang(go.step.sm/crypto)) = 0.45.0
# go.step.sm/linkedca : Apache-2.0
Provides:       bundled(golang(go.step.sm/linkedca)) = 0.20.1
# go.uber.org/automaxprocs : MIT
Provides:       bundled(golang(go.uber.org/automaxprocs)) = 1.6.0
# go.uber.org/mock : Apache-2.0
Provides:       bundled(golang(go.uber.org/mock)) = 0.4.0
# go.uber.org/multierr : MIT
Provides:       bundled(golang(go.uber.org/multierr)) = 1.11.0
# go.uber.org/zap : MIT
Provides:       bundled(golang(go.uber.org/zap)) = 1.27.0
# go.uber.org/zap/exp : MIT
Provides:       bundled(golang(go.uber.org/zap/exp)) = 0.3.0
# golang.org/x/crypto : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/crypto)) = 0.31.0
# golang.org/x/crypto/x509roots/fallback : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/crypto/x509roots/fallback)) = 71ed71b
# golang.org/x/exp : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/exp)) = 9bf2ced
# golang.org/x/mod : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/mod)) = 0.18.0
# golang.org/x/net : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/net)) = 0.33.0
# golang.org/x/sync : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/sync)) = 0.10.0
# golang.org/x/sys : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/sys)) = 0.28.0
# golang.org/x/term : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/term)) = 0.27.0
# golang.org/x/text : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/text)) = 0.21.0
# golang.org/x/time : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/time)) = 0.7.0
# golang.org/x/tools : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/tools)) = 0.22.0
# google.golang.org/genproto/googleapis/api : Apache-2.0
Provides:       bundled(golang(google.golang.org/genproto/googleapis/api)) = 5fefd90
# google.golang.org/genproto/googleapis/rpc : Apache-2.0
Provides:       bundled(golang(google.golang.org/genproto/googleapis/rpc)) = 5fefd90
# google.golang.org/grpc : Apache-2.0
Provides:       bundled(golang(google.golang.org/grpc)) = 1.67.1
# google.golang.org/protobuf : BSD-3-Clause
Provides:       bundled(golang(google.golang.org/protobuf)) = 1.35.1
# gopkg.in/natefinch/lumberjack.v2 : MIT
Provides:       bundled(golang(gopkg.in/natefinch/lumberjack.v2)) = 2.2.1
# gopkg.in/yaml.v3 : Apache-2.0 AND MIT
Provides:       bundled(golang(gopkg.in/yaml.v3)) = 3.0.1
# howett.net/plist : BSD-2-Clause-Views AND BSD-3-Clause
Provides:       bundled(golang(howett.net/plist)) = 1.0.0

BuildRequires:  systemd-rpm-macros

%{?systemd_requires}
%{?sysusers_requires_compat}
Provides:       webserver

%description
Caddy is an extensible server platform that uses TLS by default.

%prep
%autosetup -p 1 -a 1
mkdir -p src/$(dirname %{goipath})
ln -s $PWD src/%{goipath}

%build
export GO111MODULE=off
export GOPATH=$PWD
CGO_ENABLED=0 go build -trimpath -gcflags=-l -ldflags="-X %{goipath}.CustomVersion=v%{version}" -o bin/caddy %{goipath}/cmd/caddy


%install
# command
install -D -p -m 0755 -t %{buildroot}%{_bindir} bin/caddy

# man pages
./bin/caddy manpage --directory %{buildroot}%{_mandir}/man8

# config
install -D -p -m 0644 %{S:10} %{buildroot}%{_sysconfdir}/caddy/Caddyfile
install -d -m 0755 %{buildroot}%{_sysconfdir}/caddy/Caddyfile.d

# Copy post-caddy script to expected path
install -d -m 755 %{buildroot}%{_sysconfdir}/edge-node/node/confs
cp %{SOURCE3} %{buildroot}%{_sysconfdir}/edge-node/node/confs

# systemd units
install -D -p -m 0644 -t %{buildroot}%{_unitdir} %{S:20} %{S:21}

# sysusers
install -D -p -m 0644 %{S:22} %{buildroot}%{_sysusersdir}/caddy.conf

# data directory
install -d -m 0750 %{buildroot}%{_sharedstatedir}/caddy

# welcome page
install -D -p -m 0644 %{S:31} %{buildroot}%{_datadir}/caddy/poweredby.png
ln -s ../testpage/index.html %{buildroot}%{_datadir}/caddy/index.html
install -d -m 0755 %{buildroot}%{_datadir}/caddy/icons
ln -s ../../pixmaps/poweredby.png %{buildroot}%{_datadir}/caddy/icons/poweredby.png

# shell completions
install -d -m 0755 %{buildroot}%{_datadir}/bash-completion/completions
./bin/caddy completion bash > %{buildroot}%{_datadir}/bash-completion/completions/caddy
install -d -m 0755 %{buildroot}%{_datadir}/zsh/site-functions
./bin/caddy completion zsh > %{buildroot}%{_datadir}/zsh/site-functions/_caddy
install -d -m 0755 %{buildroot}%{_datadir}/fish/vendor_completions.d
./bin/caddy completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/caddy.fish


%check
# ensure that the version was embedded correctly
[[ "$(./bin/caddy version)" == "v%{version}" ]] || exit 1

# run the upstream tests
export GOPATH=$PWD
cd src/%{goipath}
%gotest ./...

%pre
%sysusers_create_compat %{S:22}

%post
chmod +x %{_sysconfdir}/edge-node/node/confs/%{SOURCE3}
%systemd_post caddy.service

if [ -x %{_sbindir}/getsebool ]; then
    # connect to ACME endpoint to request certificates
    setsebool -P httpd_can_network_connect on
fi
if [ -x %{_sbindir}/semanage -a -x %{_sbindir}/restorecon ]; then
    # file contexts
    semanage fcontext --add --type httpd_exec_t        '%{_bindir}/caddy'               2> /dev/null || :
    semanage fcontext --add --type httpd_sys_content_t '%{_datadir}/caddy(/.*)?'        2> /dev/null || :
    semanage fcontext --add --type httpd_config_t      '%{_sysconfdir}/caddy(/.*)?'     2> /dev/null || :
    semanage fcontext --add --type httpd_var_lib_t     '%{_sharedstatedir}/caddy(/.*)?' 2> /dev/null || :
    restorecon -r %{_bindir}/caddy %{_datadir}/caddy %{_sysconfdir}/caddy %{_sharedstatedir}/caddy || :
fi
if [ -x %{_sbindir}/semanage ]; then
    # QUIC
    semanage port --add --type http_port_t --proto udp 80   2> /dev/null || :
    semanage port --add --type http_port_t --proto udp 443  2> /dev/null || :
    # admin endpoint
    semanage port --add --type http_port_t --proto tcp 2019 2> /dev/null || :
fi

%preun
%systemd_preun caddy.service

%postun
%systemd_postun_with_restart caddy.service

if [ $1 -eq 0 ]; then
    if [ -x %{_sbindir}/getsebool ]; then
        # connect to ACME endpoint to request certificates
        setsebool -P httpd_can_network_connect off
    fi
    if [ -x %{_sbindir}/semanage ]; then
        # file contexts
        semanage fcontext --delete --type httpd_exec_t        '%{_bindir}/caddy'               2> /dev/null || :
        semanage fcontext --delete --type httpd_sys_content_t '%{_datadir}/caddy(/.*)?'        2> /dev/null || :
        semanage fcontext --delete --type httpd_config_t      '%{_sysconfdir}/caddy(/.*)?'     2> /dev/null || :
        semanage fcontext --delete --type httpd_var_lib_t     '%{_sharedstatedir}/caddy(/.*)?' 2> /dev/null || :
        # QUIC
        semanage port     --delete --type http_port_t --proto udp 80   2> /dev/null || :
        semanage port     --delete --type http_port_t --proto udp 443  2> /dev/null || :
        # admin endpoint
        semanage port     --delete --type http_port_t --proto tcp 2019 2> /dev/null || :
    fi
fi

%files
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/caddy
%{_mandir}/man8/caddy*.8*
%{_datadir}/caddy
%{_unitdir}/caddy.service
%{_unitdir}/caddy-api.service
%{_sysusersdir}/caddy.conf
%attr(0750,caddy,caddy) %{_sysconfdir}/caddy
%config(noreplace) %{_sysconfdir}/caddy/Caddyfile
%dir %{_sysconfdir}/caddy/Caddyfile.d
%attr(0750,caddy,caddy) %dir %{_sharedstatedir}/caddy
%{_datadir}/bash-completion/completions/caddy
%{_datadir}/zsh/site-functions/_caddy
%{_datadir}/fish/vendor_completions.d/caddy.fish
%attr(0755,caddy,caddy) %{_sysconfdir}/edge-node/node/confs/post-caddy.sh

%changelog
* Wed Apr 09 2025 Tan Jia Yong <jia.yong.tan@intel.com> - 2.9.1-10
- Include patch for CVE-2024-45339

* Mon Apr 07 2025 kintali Jayanth <kintalix.jayanth@intel.com> - 2.9.1-9
- Resolve in CVE-2025-22869.patch

* Tue Apr 01 2025 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 2.9.1-8
- Set owner, group and permissions for post-caddy.sh

* Fri Mar 28 2025 Tadeusz Matenko <tadeusz.matenko@intel.com> - 2.9.1-7
- Set owner, group and permissions for pre-caddy.sh

* Tue Mar 25 2025 Rajeev Ranjan <rajeev2.ranjan@intel.com> - 2.9.1-6
- Extend service to wait on network-online.target & add a ExecStartPre

* Fri Mar 21 2025 Anuj Mittal <anuj.mittal@intel.com> - 2.9.1-5
- Bump Release to rebuild

* Wed Feb 05 2025 Tadeusz Matenko <tadeusz.matenko@intel.com> - 2.9.1-4
- Import caddy 2.9.1 from Fedora 42
- Remove CVE-2024-45337.patch. Caddy 2.9.1 uses patched version of golang.org/x/crypto - 0.31.0

* Wed Jan 22 2025 Carl George <carlwgeorge@fedoraproject.org> - 2.9.1-3
- Run tests with -short flag like upstream to avoid test failures
- Resolves FTBFS rhbz#2339573 rhbz#2339954

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Carl George <carlwgeorge@fedoraproject.org> - 2.9.1-1
- Update to version 2.9.1 rhbz#2336409

* Wed Jan 01 2025 Carl George <carlwgeorge@fedoraproject.org> - 2.9.0-1
- Update to version 2.9.0 rhbz#2316289

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 05 2024 Carl George <carlwgeorge@fedoraproject.org> - 2.8.4-1
- Update to version 2.8.4 rhbz#2278549
- Resolves CVE-2023-49295 rhbz#2257829
- Resolves CVE-2024-27304 rhbz#2268278
- Resolves CVE-2024-27289 rhbz#2268468
- Resolves CVE-2024-28180 rhbz#2268877
- Resolves CVE-2024-22189 rhbz#2273517
- Remove LimitNPROC from systemd unit files

* Mon Feb 3 2025 Lee Chee Yang <chee.yang.lee@intel.com> - 2.7.6-9
- Include patch for CVE-2024-45337

* Tue Jan 21 2025 Christopher Nolan <christopher.nolan@intel.com> - 2.7.6-8
- Update file permissions for caddy folder

* Tue Dec 31 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 2.7.6-7
- Update Source URL.

* Wed Dec 18 2024 Christopher Nolan <christopher.nolan@intel.com> - 2.7.6-6
- Fix file permissions for caddy folder

* Tue Nov 26 2024 Andy <andy.peng@intel.com> - 2.7.6-5
- Update go build flag for size optimization
- `-l` to disable inling
- `-trimpath` to remove absolute path

* Thu Nov 21 2024 Andy <andy.peng@intel.com> - 2.7.6-4
- Update go build flag for size optimization

* Wed Jul 17 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 2.7.6-3
- Initial Edge Microvisor Toolkit import from Fedora 40 (license: MIT). License verified.
- Fixed bash completion installation dir path
- Fixed zsh completion installation dir path
- Fixed fish completion installation dir path
- Removed un-unsed checks

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 2.7.6-2
- Rebuild for golang 1.22.0

* Fri Feb 09 2024 Carl George <carlwgeorge@fedoraproject.org> - 2.7.6-1
- Update to version 2.7.6 rhbz#2253698
- Includes fix for CVE-2023-45142 rhbz#2246587

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 30 2023 Carl George <carlwgeorge@fedoraproject.org> - 2.7.5-1
- Update to version 2.7.5
- Update poweredby logos
- Add symlink for system_noindex_logo.png on EL9
- Symlink directly to fedora-testpage directory on Fedora

* Thu Aug 17 2023 Carl George <carlwgeorge@fedoraproject.org> - 2.7.4-1
- Update to version 2.7.4, resolves rhbz#2232696
- Fix CVE-2023-3978, resolves rhbz#2229582

* Tue Aug 08 2023 Carl George <carl@george.computer> - 2.7.3-1
- Update to version 2.7.3, resolves rhbz#2229638

* Thu Aug 03 2023 Carl George <carl@george.computer> - 2.7.2-1
- Update to version 2.7.2, resolves rhbz#2228776

* Thu Jul 27 2023 Carl George <carl@george.computer> - 2.7.0~beta2-1
- Update to version 2.7.0~beta2, resolves rhbz#2225732 rhbz#2124366
- Resolves CVE-2022-41717 rhbz#2164315
- Resolves CVE-2022-41723 rhbz#2178412
- Add man pages
- Use generated shell completion files instead of static ones
- Add fish shell completions
- Switch to systemd sysusers

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 24 2023 Carl George <carl@george.computer> - 2.5.2-3
- Rebuild for CVE-2022-41717 in golang

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 09 2022 Carl George <carl@george.computer> - 2.5.2-1
- Latest upstream, resolves rhbz#2062499 rhbz#2113136

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 2.4.6-4
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Fri Jun 17 2022 Robert-André Mauchin <zebob.m@gmail.com> - 2.4.6-3
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Fri Feb 25 2022 Carl George <carl@george.computer> - 2.4.6-2
- Update welcome page symlink and image to work on both Fedora and EPEL

* Wed Feb 16 2022 Carl George <carl@george.computer> - 2.4.6-1
- Latest upstream rhbz#1984163

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 03 2021 Carl George <carl@george.computer> - 2.3.0-1
- Latest upstream
- Fix vendored license handling
- Switch to white logo rhbz#1934864

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.1-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 2020 Carl George <carl@george.computer> - 2.2.1-1
- Latest upstream

* Sat Sep 26 2020 Carl George <carl@george.computer> - 2.2.0-1
- Latest upstream

* Sat Sep 19 2020 Carl George <carl@george.computer> - 2.2.0~rc3-1
- Latest upstream

* Fri Aug 14 2020 Carl George <carl@george.computer> - 2.1.1-2
- Add bash and zsh completion support

* Sun Aug 09 2020 Carl George <carl@george.computer> - 2.1.1-1
- Update to Caddy v2
- Remove all v1 plugins
- Use vendored dependencies
- Remove devel subpackage
- Rename config file per upstream request
- Use webserver test page from system-logos-httpd

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 20:56:10 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.4-1
- Update to 1.0.4 (#1803691)

* Mon Feb 17 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.3-3
- Rebuilt for GHSA-jf24-p9p9-4rjh

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 07 2019 Carl George <carl@george.computer> - 1.0.3-1
- Latest upstream
- Remove bundled lego and plugins
- Remove dyn, gandi, namecheap, and rfc2136 dns providers
- Add patch0 to fix `-version` flag
- Add patch1 to adjust blackfriday import path
- Add devel subpackages
- Run test suite

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Carl George <carl@george.computer> - 0.11.4-2
- Switch unit file from ProtectSystem strict to full rhbz#1706651

* Wed Mar 06 2019 Carl George <carl@george.computer> - 0.11.4-1
- Latest upstream
- Update bundled dnsproviders to 0.1.3
- Update bundled lego to 2.2.0
- Enable googlecloud, route53, and azure dns providers on epel7
- Allow custom http port with default config file rhbz#1685446

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Carl George <carl@george.computer> - 0.11.1-2
- Buildrequires at least golang 1.10

* Tue Nov 13 2018 Carl George <carl@george.computer> - 0.11.1-1
- Latest upstream
- Update bundled geoip

* Fri Oct 19 2018 Carl George <carl@george.computer> - 0.11.0-3
- Enable httpd_can_network_connect selinux boolean to connect to ACME endpoint rhbz#1641158
- Define UDP 80/443 as selinux http_port_t for QUIC rhbz#1608548
- Define TCP 5033 as selinux http_port_t for HTTP challenge rhbz#1641160

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 12 2018 Carl George <carl@george.computer> - 0.11.0-1
- Latest upstream

* Sat Apr 21 2018 Carl George <carl@george.computer> - 0.10.14-1
- Latest upstream
- Overhaul %%prep to extract everything with %%setup
- Edit lego providers to require acmev2 instead of acme
- Add provides for specific providers from %%import_path_dnsproviders and %%import_path_lego
- Add azure dns provider on f28+

* Fri Apr 20 2018 Carl George <carl@george.computer> - 0.10.11-6
- Enable geoip plugin on EL7
- Only provide bundled geoip/realip/dnsproviders/lego when the respective plugin is enabled

* Wed Apr 18 2018 Carl George <carl@george.computer> - 0.10.11-5
- Add geoip plugin

* Tue Apr 17 2018 Carl George <carl@george.computer> - 0.10.11-4
- Correct ExclusiveArch fallback

* Mon Apr 16 2018 Carl George <carl@george.computer> - 0.10.11-3
- Enable s390x
- Disable googlecloud and route53 dns providers on EL7 due to dependency issues

* Fri Mar 30 2018 Carl George <carl@george.computer> - 0.10.11-2
- Add googlecloud dns provider
- Add route53 dns provider
- Set minimum golang version to 1.9
- Set selinux labels in scriptlets

* Sat Feb 24 2018 Carl George <carl@george.computer> - 0.10.11-1
- Latest upstream

* Sat Feb 24 2018 Carl George <carl@george.computer> - 0.10.10-4
- Change ProtectSystem from strict to full in unit file on RHEL

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Carl George <carl@george.computer> - 0.10.10-2
- Add powerdns provider

* Mon Oct 09 2017 Carl George <carl@george.computer> - 0.10.10-1
- Latest upstream

* Mon Oct 02 2017 Carl George <carl@george.computer> - 0.10.9-6
- Add provides for bundled libraries

* Mon Oct 02 2017 Carl George <carl@george.computer> - 0.10.9-5
- Enable rfc2136 dns provider
- List plugins in description

* Mon Sep 18 2017 Carl George <carl@george.computer> - 0.10.9-4
- Exclude s390x

* Sun Sep 17 2017 Carl George <carl@george.computer> - 0.10.9-3
- Add realip plugin
- Add conditionals for plugins

* Sat Sep 16 2017 Carl George <carl@george.computer> - 0.10.9-2
- Add sources for caddyserver/dnsproviders and xenolf/lego
- Disable all dns providers that require additional libraries (dnsimple, dnspod, googlecloud, linode, ovh, route53, vultr)
- Rewrite default index.html

* Tue Sep 12 2017 Carl George <carl@george.computer> - 0.10.9-1
- Latest upstream
- Add config validation to unit file
- Disable exoscale dns provider https://github.com/xenolf/lego/issues/429

* Fri Sep 08 2017 Carl George <carl@george.computer> - 0.10.8-1
- Latest upstream
- Build with %%gobuild macro
- Move config subdirectory from /etc/caddy/caddy.conf.d to /etc/caddy/conf.d

* Tue Aug 29 2017 Carl George <carl@george.computer> - 0.10.7-1
- Latest upstream

* Fri Aug 25 2017 Carl George <carl@george.computer> - 0.10.6-2
- Use SIQQUIT to stop service
- Increase the process limit from 64 to 512
- Only `go get` in caddy/caddymain

* Fri Aug 11 2017 Carl George <carl@george.computer> - 0.10.6-1
- Latest upstream
- Add webserver virtual provides
- Drop tmpfiles and just own /var/lib/caddy directly
- Remove PrivateDevices setting from unit file, it prevents selinux process transitions
- Disable rfc2136 dns provider https://github.com/caddyserver/dnsproviders/issues/11

* Sat Jun 03 2017 Carl George <carl.george@rackspace.com> - 0.10.3-2
- Rename Envfile to envfile
- Rename Caddyfile to caddy.conf
- Include additional configs from caddy.conf.d directory

* Fri May 19 2017 Carl George <carl.george@rackspace.com> - 0.10.3-1
- Latest upstream

* Mon May 15 2017 Carl George <carl.george@rackspace.com> - 0.10.2-1
- Initial package

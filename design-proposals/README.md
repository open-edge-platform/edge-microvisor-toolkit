# Proposing Features and Changes to Edge Microvisor Toolkit

## Introduction

The development process of components in the Open Edge Platform is
design-driven. Significant changes to the components, installation
scripts, packages, image configurations, or tools must be first
discussed, formally documented and agreed upon before they can be implemented.

This document describes the process for proposing, documenting, and
implementing changes.

To learn more about the different components please check
the [Edge Microvisor Toolkit](https://docs.openedgeplatform.intel.com/edge-microvisor-toolkit/3.0/docs/index.html)

## The Proposal Process

The proposal process is the process for reviewing a proposal and reaching
a decision about whether to accept or decline the proposal.

1. The author of the proposal creates [a Github issue](https://github.com/open-edge-platform/edge-microvisor-toolkit/issues) 
with the `Feature Request` template, briefly describing the new feature.

   >Note: There is no need for a design proposal document at this point.

2. Maintainers of the overall project discuss the issue and decide on one of three outcomes:
    - Accept the feature request.
    - Decline the feature request.
    - Ask for a [Design Document](#design-documents) that, if merged, becomes an 
      `Architecture Decision Record` (ADR).

   If the feature request is accepted or declined, the process is done.
   Otherwise the discussion is expected to identify concerns that
   should be addressed in more detail in the design document.

3. If the [Design Document](#design-documents) is requested, the author of the proposed
   changes creates it, working out its details and addressing the concerns raised in
   the initial discussion. The author creates a Pull Request in the `edge-microvisor-toolkit`
   repository, assigns it the `Proposal` label, and adds a link to it in the
   original feature issue.

4. Once comments and revisions on the design doc are resolved, the final discussion of the
   issue leads to one of two outcomes:
    - Accept design document and related feature by merging the Pull Request.
    - Decline proposal, by closing the Pull Request without merging.

5. If the pull request with the Design Document is merged, it means the design is accepted
   as described there, and it becomes an **ADR, Architecture Decision Record**.

After the Pull Request is merged or closed, and its corresponding design is
accepted or declined (whether after step 2 or step 4), implementation work
proceeds in the same way as for any other contribution.

## Detail

### Goals

- Make sure that proposals get a proper, fair, timely, recorded evaluation with
a clear answer.
- Make past proposals easy to find, to avoid duplicated effort.
- If a design document is needed, make sure contributors know how to write a
good one.

### Definitions

- A **proposal** is a suggestion filed as a Feature Request GitHub issue,
  identified by having the Proposal label.
- A **design document**, is the expanded form of a proposal, written when the
proposal needs more careful explanation and consideration.
- An **ADR, Architecture Decision Record** is the merged version of the
**design document**.

### Scope

The proposal process should be used for any notable change or addition to the
language, libraries, and tools. “Notable” includes (but is not limited to):

- New features, such as the addition of a new component or a feature.
- Build infrastructure changes.
- Any other behavior changes in existing functionality.
- Adoption or use of new protocols, protocol versions, cryptographic algorithms,
  and the like, even in an implementation.

Because proposals begin (and will often end) with the filing of a Feature Request
issue, even small changes can go through the proposal process if appropriate.
Deciding what is appropriate is a matter of judgment that is constantly refined.
If in doubt, do file a proposal.

### Design Documents

As noted above, some (but not all) proposals need to be elaborated on in a design
document.

- The design document should be checked in to 
  [the proposal directory](https://github.com/open-edge-platform/edge-microvisor-toolkit/design-proposals/)
  as `EMT-shortname.md`, where `shortname` is a few dash-separated words at most.

- The design doc should follow [the template](./design-proposal-template.md).

- The design doc should address any specific concerns raised during the initial
  discussion.

- It is expected that the design doc may go through multiple checked-in
  revisions.

- For ease of review with Github, design documents should be compliant with
  the `markdownlit` rules express in this
- repo, that will be checked by `CI`. The writer can check conformace by issuing
the `make lint` command.

### Quick Start for Experienced Committers

Experienced committers who are certain that a design doc will be required for a
particular proposal can skip steps 1 and 2 and include the design document with
the initial issue.

In the worst case, skipping these steps only leads to an unnecessary design doc.

### Proposal Review

The proposal will be discussed in the pull request and if needed one or more
online calls will be established. At the end of the discussion, the repo
maintainer(s) for the code involved will have the last say in changing the
pull request status to 'Active', 'Accepted', or 'Declined'.

#### Active

Issues in the Active column are reviewed weekly by different teams. Track them
to see emerging consensus in the discussions. The maintainers may also comment, make
suggestions, ask clarifying questions, and try to restate the proposals to make
sure everyone agrees about what exactly is being discussed.

#### Accepted

Once a proposal is marked as Accepted, the pull request is merged or the Issue
is closed, the Proposal-Accepted label is applied, and the accepted design is put
in the `/design-proposals` folder.

A release label may be added to signify which release of the Edge Microvisor
Toolkit is going to include the proposal.

#### Declined

A proposal is marked as Declined if a complete re-work is needed, change is not
required anymore or not applicable. Once a proposal is Declined, the Pull
request or the Feature Request it is closed.

## Help

If you need help with this process, please contact the Project's mantainers
contributors by posting to the [Discussions](https://github.com/open-edge-platform/edge-manageability-framework/discussions).

To learn about contributing to Edge Microvisor Toolkit in general, see the
[contribution guidelines](https://docs.openedgeplatform.intel.com/edge-microvisor-toolkit/3.0/docs/developer-guide/contribution/index.html).

---
title: Someone just pushed
assignees: {{ payload.sender.login }}
labels: enhancement
---
Someone just pushed, oh no! Here's who did it: {{ payload.sender.login }}.
PR #{{ pullRequest.pull_number }}

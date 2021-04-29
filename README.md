this applications returns the information about all of the credhub services instances that are bound to it.
one can combine this with jq to create shell based actions or chain into an automation workflow.

make sure to update the manifests with the credhub service instances it is bound to

curl <approute>/credhub_info | jq 

```
Thu Apr 29 01:20:11 PM - ttys001
anishpatel@anpatel-a01 : ~
→ curl -s  http://walk-credhub.apps.tas02.azure.buildit.sh/credhub_info | jq         JOBS: 0
[
  {
    "binding_name": null,
    "credentials": {
      "entry": 1,
      "key1": "value1",
      "key2": "value2"
    },
    "instance_name": "test-credhub",
    "label": "credhub",
    "name": "test-credhub",
    "plan": "default",
    "provider": null,
    "syslog_drain_url": null,
    "tags": [
      "credhub"
    ],
    "volume_mounts": []
  },
  {
    "binding_name": null,
    "credentials": {
      "entry": 1,
      "key1": "value1",
      "key2": "value2"
    },
    "instance_name": "test-credhub-2",
    "label": "credhub",
    "name": "test-credhub-2",
    "plan": "default",
    "provider": null,
    "syslog_drain_url": null,
    "tags": [
      "credhub"
    ],
    "volume_mounts": []
  }
]
```

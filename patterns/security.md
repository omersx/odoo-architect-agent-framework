# Pattern: Security

New model means new access rights.

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_my_model_user,my.model user,model_my_model,base.group_user,1,1,1,0
```

Inherited models usually keep their existing access rights. Still review whether the new fields expose sensitive data, need group restrictions, or require record rules.

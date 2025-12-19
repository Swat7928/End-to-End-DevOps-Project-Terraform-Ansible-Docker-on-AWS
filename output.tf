############################################
# Outputs (Ansible Inventory Ready)
############################################
output "bastion_private_ip" {
  value = aws_instance.bastion.private_ip
}

output "app_private_ip" {
  value = aws_instance.app.private_ip
}

output "db_private_ip" {
  value = aws_instance.db.private_ip
}

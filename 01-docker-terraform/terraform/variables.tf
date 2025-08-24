variable "credentials" {
  description = "My Credentials"
  default     = "./keys/terraform-demo-470008-eefd27a592f9.json"
}

variable "project" {
  description = "Project"
  default     = "terraform-demo-470008"
}

variable "location" {
  description = "Project Location"
  default     = "EU"
}

variable "region" {
  description = "Project Region"
  default     = "europe-west1"
}

variable "bq_dataset_name" {
  description = "My Big Query Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "terraform-demo-470008-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

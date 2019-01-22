# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *


class LamaTemplateInline(admin.TabularInline):
    model = LamaTemplate
    fk_name = 'source_sid'  # or 'world', as applicable.
    extra = 0

class ServiceInline(admin.TabularInline):
    model = Service
    fk_name = 'system'  # or 'world', as applicable.
    extra = 0


# Register your models here.
class ClusterAvailabilityLevelAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class ClusterCpuOversubscriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class ClusterMemoryOversubscriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class CpuArchitectureAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "cores", "threads", "max_hana_prod_vms_per_socket",)
    fields = ("display_name", "cores", "threads", "max_hana_prod_vms_per_socket",)


class CustomRamAngeAdmin(admin.ModelAdmin):
    list_display = ("id", "ram_start", "ram_end", "steps", "unit",)
    fields = ("ram_start", "ram_end", "steps", "unit",)


class DatabaseTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class DisasterRecoveryTenancyAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class EncryptionStateAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class EsxHostCpuOversubscriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class EsxHostMemoryOversubscriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class EventOriginAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class EventourceAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class EventtatusAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class EventTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class HostStateAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class Hp3parTierAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class IpAddressAllocationStateAdmin(admin.ModelAdmin):
    list_display = ("id", "allocation_state", "value",)
    fields = ("allocation_state", "value",)


class IpAddressAllocationPurposeAdmin(admin.ModelAdmin):
    list_display = ("id", "allocation_purpose", "value",)
    fields = ("allocation_purpose", "value",)


class LamaTemplateStateAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class LamaTemplateStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class LicenseEventTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class LifecycleActionTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class LifecycleStateAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class LvmLevelAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class LvmTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class MacAddressAllocationStateAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class MigrationStateAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class SapOfferingAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class ServiceLevelAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class ServiceRoleAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class SidOriginAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class SidTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class StorageStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class StorageTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value", "store_type_logo",)
    fields = ("id", "display_name", "value", "store_type_logo",)


class StorageWorkloadTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "max_num_of_prod_inst_hosts", "value",)
    fields = ("display_name", "max_num_of_prod_inst_hosts", "value",)


class SubscriptionStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class SuitabilityAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class TicketClosureCodeInterpretationAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class TicketImplementationStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class TicketOriginAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class TickettateAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class TicketTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class TopologyAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class VirtualizationAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class VlanRoleAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class VlanTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class VolumeGroupTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class VolumeTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class WorkloadTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class ZoneAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value",)
    fields = ("display_name", "value",)


class DataCenterAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "legacy_vpc_name", "display_name", "region", "country_code", "timezone", "dual_dc_pair",
                    "secondary_site",
                    # "paired_datacenter",
                    "pci_enabled", "disaster_recovery_enabled", "disaster_recovery_site_name", "country",
                    "iso_3166_01_code",
                    "location_currency_code", "location_currency_symbol", "location", "service_delivery_manager_name",
                    "service_delivery_manager_email", "site_technical_coordinator_name",
                    "site_technical_coordinator_email",
                    "provisioning_coordinator_name", "provisioning_coordinator_email",)
    fields = (
        "legacy_vpc_name", "display_name", "region", "country_code", "timezone", "dual_dc_pair",
        "secondary_site",
        # "paired_datacenter",
        "pci_enabled", "disaster_recovery_enabled", "disaster_recovery_site_name", "country",
        "iso_3166_01_code",
        "location_currency_code", "location_currency_symbol", "location", "service_delivery_manager_name",
        "service_delivery_manager_email", "site_technical_coordinator_name",
        "site_technical_coordinator_email",
        "provisioning_coordinator_name", "provisioning_coordinator_email",)


class VcenterAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "name", "host", "ip", "username", "password", "port", "vmware_dc", "datacenter", "zone",
                    "lfecycle_state",
                    "asser_tag", "capacity_team_model_name", "capacity_team_device_registration_name", "annotation",)
    fields = (
        "name", "host", "ip", "username", "password", "port", "vmware_dc", "datacenter", "zone",
        "lfecycle_state",
        "asser_tag", "capacity_team_model_name", "capacity_team_device_registration_name", "annotation",)


class TenantAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "datacenter", "name", "display_name", "esl_customer_name", "esl_company_id",
                    "company_id_for_storage_naming",
                    "email_distribution", "hmco_action",)
    fields = (
        "datacenter", "name", "display_name", "esl_customer_name", "esl_company_id",
        "company_id_for_storage_naming",
        "email_distribution", "hmco_action",)


class ClusterAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "name", "vcenter", "data_center", "lifecycle_state", "cpu_oversubscription",
                    "warn_cpu_oversubscription_pct", "alert_cpu_oversubscription_pct", "lca_cpu_oversubscription_pct",
                    "make_unavailable_cpu_oversubscription_pct", "last_known_cpu_oversubscription_pct",
                    "memory_oversubscription",
                    "warn_memory_oversubscription_pct", "alert_memory_oversubscription_pct",
                    "lca_memory_oversubscription_pct",
                    "make_unavailable_memory_oversubscription_pct", "last_known_memory_oversubscription_pct",
                    "max_num_of_rdm",
                    "warn_rdm_oversubscription_pct", "alert_rdm_oversubscription_pct", "lca_rdm_oversubscription_pct",
                    "make_unavailable_rdm_oversubscription_pct", "last_known_num_of_rdm", "asset_tag",
                    "capacity_team_model_name",
                    "capacity_team_device_registration_name", "manual_override", "annotation", "last_updated_on",)
    fields = (
        "name", "vcenter", "data_center", "lifecycle_state", "cpu_oversubscription",
        "warn_cpu_oversubscription_pct", "alert_cpu_oversubscription_pct", "lca_cpu_oversubscription_pct",
        "make_unavailable_cpu_oversubscription_pct", "last_known_cpu_oversubscription_pct",
        "memory_oversubscription",
        "warn_memory_oversubscription_pct", "alert_memory_oversubscription_pct",
        "lca_memory_oversubscription_pct",
        "make_unavailable_memory_oversubscription_pct", "last_known_memory_oversubscription_pct",
        "max_num_of_rdm",
        "warn_rdm_oversubscription_pct", "alert_rdm_oversubscription_pct", "lca_rdm_oversubscription_pct",
        "make_unavailable_rdm_oversubscription_pct", "last_known_num_of_rdm", "asset_tag",
        "capacity_team_model_name",
        "capacity_team_device_registration_name", "manual_override", "annotation", "last_updated_on",)


class Hp3parAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "display_name", "name", "zone", "storageworkload", "ip", "url", "username", "password",
                    "datacenter",
                    "lifecycle_state", "asset_tag", "capacity_team_model_name", "capacity_tea_device_registration_name",
                    "manual_override", "annotation",)
    fields = (
        "display_name", "name", "zone", "storageworkload", "ip", "url", "username", "password",
        "datacenter",
        "lifecycle_state", "asset_tag", "capacity_team_model_name", "capacity_tea_device_registration_name",
        "manual_override", "annotation",)


class CpgAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "display_name", "type", "domain", "the_volume_set_must_be_used", "dedicated_to_a_tenant",
        "virtual_volume_set", "highly_available", "dr_replication", "hp3par", "tenant",)
    fields = (
        "name", "display_name", "type", "domain", "the_volume_set_must_be_used", "dedicated_to_a_tenant",
        "virtual_volume_set", "highly_available", "dr_replication", "hp3par", "tenant",)


class CustomCpuValueAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "cpuarchitecture", "vcpu", "socket",)
    fields = ("display_name", "cpuarchitecture", "vcpu", "socket",)


class TierAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description",)
    fields = ("name", "description",)


class CustomSizeAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "tier", "customcpuvalue", "customramrange",)
    fields = ("display_name", "tier", "customcpuvalue", "customramrange",)


class DatastoreAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "display_name", "name", "storage_type", "cluster", "dr_replication", "dedicated_to_a_tenant",
                    "lifecycle_state", "total_capacity", "reserved_capacity", "warn_pct", "alert_pct", "lca_pct",
                    "make_unavailable_pct", "last_known_oversubscription_pct", "warn_vmdk_pct", "alert_vmdk_pct",
                    "lca_vmdk_pct",
                    "make_unavailable_vmdk_pct", "last_known_vmdk_pct", "manual_override", "last_updated_on",)
    fields = (
        "display_name", "name", "storage_type", "cluster", "dr_replication", "dedicated_to_a_tenant",
        "lifecycle_state", "total_capacity", "reserved_capacity", "warn_pct", "alert_pct", "lca_pct",
        "make_unavailable_pct", "last_known_oversubscription_pct", "warn_vmdk_pct", "alert_vmdk_pct",
        "lca_vmdk_pct",
        "make_unavailable_vmdk_pct", "last_known_vmdk_pct", "manual_override", "last_updated_on",)


class EsxHostAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "cluster", "cpuarchitecture", "fqdn", "socket", "hyperthreading", "ram", "lifecycle_state",
                    "asset_tag",
                    "capacity_team_model_name", "capacity_team_device_registration_name", "annotation",)
    fields = (
        "cluster", "cpuarchitecture", "fqdn", "socket", "hyperthreading", "ram", "lifecycle_state",
        "asset_tag",
        "capacity_team_model_name", "capacity_team_device_registration_name", "annotation",)


class EventCodeAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "template", "supplier", "type", "category", "source", "origin", "reference_code", "summary",
                    "description",
                    "annotation",)
    fields = (
        "template", "supplier", "type", "category", "source", "origin", "reference_code", "summary",
        "description",
        "annotation",)


class LvmAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "name", "type", "lvm_host", "lvm_username", "lvm_password", "lvm_url", "datacenter",
                    "lifecycle_state",)
    fields = (
        "name", "type", "lvm_host", "lvm_username", "lvm_password", "lvm_url", "datacenter",
        "lifecycle_state",)


class OrderTrackingAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "tenant", "product_uuid", "product_name", "order_id", "order_uuid", "supplier_request_id",
                    "order_item_id",
                    "subscription_uuid", "subscription_instance_component_uuid", "subscription_owner_id",)
    fields = (
        "tenant", "product_uuid", "product_name", "order_id", "order_uuid", "supplier_request_id",
        "order_item_id",
        "subscription_uuid", "subscription_instance_component_uuid", "subscription_owner_id",)


class SystemAdmin(admin.ModelAdmin):
    inlines = [LamaTemplateInline,ServiceInline]

    list_display = ("id", "datacenter", "lvm_host", "lama_host", "sap_sid", "primary_system",
                    # "source",
                    "lvm_serviceid", "tenant", "subscription_status", "backup_enabled", "highly_available",
                    "service_level", "eu_data_privacy_support", "disaster_recovery_enabled",
                    "disaster_recovery_infrastructure_tenancy_preference", "lvm_level", "hana_configuration",
                    "database_type", "sid_type", "workload_type", "sap_offering", "order_tracking", "migration_state",)
    fields = ("datacenter", "lvm_host", "lama_host", "sap_sid", "primary_system",
              # "source",
              "lvm_serviceid", "tenant", "subscription_status", "backup_enabled", "highly_available",
              "service_level", "eu_data_privacy_support", "disaster_recovery_enabled",
              "disaster_recovery_infrastructure_tenancy_preference", "lvm_level", "hana_configuration",
              "database_type", "sid_type", "workload_type", "sap_offering", "order_tracking", "migration_state",)


class TicketClosureCodeAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "value", "interpretation", "test_mode",)
    fields = ("display_name", "value", "interpretation", "test_mode",)


class TicketAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "sm9_endpoint", "billable", "company_id", "location_id", "management_region", "user_id",
                    "emergency_change",
                    "ticket_id", "type", "origin", "order", "action_request_id", "category", "last_known_state",
                    "closure_code",
                    "implementation_status", "created_on",)
    fields = (
        "sm9_endpoint", "billable", "company_id", "location_id", "management_region", "user_id",
        "emergency_change",
        "ticket_id", "type", "origin", "order", "action_request_id", "category", "last_known_state",
        "closure_code",
        "implementation_status", "created_on",)


class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "datacenter", "tenant", "username", "code", "status", "sid", "ticket",
                    # "source_event",
                    "incident", "message",)
    fields = ("datacenter", "tenant", "username", "code", "status", "sid", "ticket",
              # "source_event",
              "incident", "message",)


class Hp3parCapacityAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "hp3par", "tier", "total_capacity", "reserved_capacity", "free_capacity", "warn_pct", "alert_pct",
                    "lca_pct",
                    "make_unavailable_pct", "warn_phy_pct", "alert_phy_pct", "lca_phy_pct", "make_unavailable_phy_pct",
                    "last_known_tier_oversubscription_pct", "last_known_tier_utilization_pct", "last_updated_on",)
    fields = (
        "hp3par", "tier", "total_capacity", "reserved_capacity", "free_capacity", "warn_pct", "alert_pct",
        "lca_pct",
        "make_unavailable_pct", "warn_phy_pct", "alert_phy_pct", "lca_phy_pct", "make_unavailable_phy_pct",
        "last_known_tier_oversubscription_pct", "last_known_tier_utilization_pct", "last_updated_on",)


class Hp3parPairAdmin(admin.ModelAdmin):
    list_display = ("id", "zone1_3par", "zone2_3par", "dr_partner_array_name",)
    fields = ("zone1_3par", "zone2_3par", "dr_partner_array_name",)


class OperatingSystemAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "display_name", "value", "type", "virtualization", "username", "password", "goe_os_version",
                    "glance_id",
                    "location",)
    fields = (
        "display_name", "value", "type", "virtualization", "username", "password", "goe_os_version",
        "glance_id",
        "location",)


class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "operatingSystem", "vcenter", "supported_for_hana",)
    fields = ("name", "operatingSystem", "vcenter", "supported_for_hana",)


class SizeAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "display_name", "cpu", "socket", "ram", "system_disk", "virtualization", "cpuarchitecture",
                    "lifecycle_state", "tier",)
    fields = (
        "display_name", "cpu", "socket", "ram", "system_disk", "virtualization", "cpuarchitecture",
        "lifecycle_state", "tier",)


class VlanAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "display_name", "vlanid", "type", "role", "only_for_eso4sap_use", "netword", "mask", "gateway",
                    "range_start",
                    "range_end", "dns1", "dns2", "ntp", "byoip_enabled", "byoip_subnet", "byoip_range_start",
                    "byoip_range_end",
                    "public_ip_enabled", "public_ip_subnet", "public_ip_range_start", "public_ip_range_end",
                    "load_balance_enabled",
                    "tenant", "datacenter", "lifecycle_state",)
    fields = (
        "display_name", "vlanid", "type", "role", "only_for_eso4sap_use", "netword", "mask", "gateway",
        "range_start",
        "range_end", "dns1", "dns2", "ntp", "byoip_enabled", "byoip_subnet", "byoip_range_start",
        "byoip_range_end",
        "public_ip_enabled", "public_ip_subnet", "public_ip_range_start", "public_ip_range_end",
        "load_balance_enabled",
        "tenant", "datacenter", "lifecycle_state",)


class InstanceHostAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "hostname", "fqdn", "cpuarchitecture", "core", "socket", "cpucount", "memory",
                    "is_user_defined_size", "size",
                    "operatingSystem", "saps", "administrator_name", "administrator_password", "type", "cluster",
                    "esxhost",
                    "datastore", "hp3par", "production_vlan", "production_vlan_ip_address", "fsr_vlan",
                    "hsr_vlan_ip_address",
                    "internal_management_vlan", "internal_management_vlan_ip_address", "state", "backup_enabled",
                    "migration_state",
                    "encryption_state", "order_tracking", "suitability", "zone", "is_goe_provisioned",)
    fields = (
        "hostname", "fqdn", "cpuarchitecture", "core", "socket", "cpucount", "memory",
        "is_user_defined_size", "size",
        "operatingSystem", "saps", "administrator_name", "administrator_password", "type", "cluster",
        "esxhost",
        "datastore", "hp3par", "production_vlan", "production_vlan_ip_address", "fsr_vlan",
        "hsr_vlan_ip_address",
        "internal_management_vlan", "internal_management_vlan_ip_address", "state", "backup_enabled",
        "migration_state",
        "encryption_state", "order_tracking", "suitability", "zone", "is_goe_provisioned",)


class NicTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "nic_id", "vlan_role",)
    fields = ("nic_id", "vlan_role",)


class IpAddressPoolAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "vlan", "ipv4_address", "ipv6_address", "hostname", "dns_suffix", "fqdn", "allocation_purpose",
                    "allocation_state",)
    fields = (
        "vlan", "ipv4_address", "ipv6_address", "hostname", "dns_suffix", "fqdn", "allocation_purpose",
        "allocation_state",)


class MacAddressPoolAdmin(admin.ModelAdmin):
    list_display = ("id", "datacenter", "mac_address", "allocation_state", "allocated_on",)
    fields = ("datacenter", "mac_address", "allocation_state", "allocated_on",)


class InstanceHostNicConfigAdmin(admin.ModelAdmin):
    list_display = ("id", "instancehost", "nic_type", "vlan", "ip_address", "mac_address",)
    fields = ("instancehost", "nic_type", "vlan", "ip_address", "mac_address",)


class LamaTemplateTargetSidInstanceHostAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "hostname", "fqdn", "is_user_defined_size", "size", "socket", "core", "cpuarchitecture", "cpucount",
                    "memory",
                    "operatingSystem", "type", "cluster", "datastore", "production_vlan", "production_vlan_ip_address",
                    "hsr_vlan",
                    "hsr_vlan_ip_address", "internal_management_vlan", "internal_management_vlan_ip_address", "zone",
                    "migration_state",
                    "encryption_state",)
    fields = (
        "hostname", "fqdn", "is_user_defined_size", "size", "socket", "core", "cpuarchitecture", "cpucount",
        "memory",
        "operatingSystem", "type", "cluster", "datastore", "production_vlan", "production_vlan_ip_address",
        "hsr_vlan",
        "hsr_vlan_ip_address", "internal_management_vlan", "internal_management_vlan_ip_address", "zone",
        "migration_state",
        "encryption_state",)


class LamaTemplateTargetSidInstanceHostNicConfigAdmin(admin.ModelAdmin):
    list_display = ("id", "instancehost", "nic_type", "vlan", "ip_address", "mac_address",)
    fields = ("instancehost", "nic_type", "vlan", "ip_address", "mac_address",)


class LifecycleActionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type", "description",)
    fields = ("name", "type", "description",)


class LamaTemplateAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "display_name", "description", "action", "lama", "lama_template_name", "lama_template_id",
                    "source_sid",
                    "refresh_using_sid", "state", "status", "request_description", "author_annotation",)
    fields = (
        "display_name", "description", "action", "lama", "lama_template_name", "lama_template_id",
        "source_sid",
        "refresh_using_sid", "state", "status", "request_description", "author_annotation",)


class LamaTemplateTargetSidAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "template", "display_name", "primary_system", "datacenter", "tenant", "backup_enabled",
                    "highly_available",
                    "workload_type", "service_level", "eu_data_privacy_support", "disaster_recovery_enabled",
                    "disaster_recovery_infrastructure_tenancy_preference", "lvm_level", "hana_configuration",
                    "database_type",
                    "sid_type", "sap_offering", "migration_state",)
    fields = (
        "template", "display_name", "primary_system", "datacenter", "tenant", "backup_enabled",
        "highly_available",
        "workload_type", "service_level", "eu_data_privacy_support", "disaster_recovery_enabled",
        "disaster_recovery_infrastructure_tenancy_preference", "lvm_level", "hana_configuration",
        "database_type",
        "sid_type", "sap_offering", "migration_state",)


class ServiceRoleDetailAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "display_name", "value", "servicerole", "includes_eao_sap_application_support", "tenant",
                    "lifecycle_state",
                    "service_logo",)
    fields = (
        "display_name", "value", "servicerole", "includes_eao_sap_application_support", "tenant",
        "lifecycle_state",
        "service_logo",)


class LamaTemplateTargetSidServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "sid", "service_role", "service_role_detail", "topology",)
    fields = ("sid", "service_role", "service_role_detail", "topology",)


class LamaTemplateTargetSidVolumeAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "cpg", "datastore", "volume_type", "display_name", "size", "cg_name", "volumegrouptype",
                    "instance_host",
                    "migration_state", "encryption_state",)
    fields = (
        "cpg", "datastore", "volume_type", "display_name", "size", "cg_name", "volumegrouptype",
        "instance_host",
        "migration_state", "encryption_state",)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "system", "service_role", "service_role_detail", "topology",)
    fields = ("system", "service_role", "service_role_detail", "topology",)


class Service_vipAdmin(admin.ModelAdmin):
    list_display = ("id", "service", "vlan", "ip_address", "description",)
    fields = ("service", "vlan", "ip_address", "description",)


class SidLvmLicenseEventAdmin(admin.ModelAdmin):
    list_display = ("id", "sid", "lvm_level", "event_type",)
    fields = ("sid", "lvm_level", "event_type",)


class TenantUserGroupAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "tenant",)
    fields = ("name", "tenant",)


class VlanTripletAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "production_vlan", "internal_management_vlan", "hsr_vlan", "lifecycle_state",)
    fields = ("display_name", "production_vlan", "internal_management_vlan", "hsr_vlan", "lifecycle_state",)


class VlaAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "lvm_host", "url", "username", "password",)
    fields = ("name", "lvm_host", "url", "username", "password",)


class VmnetworkAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "vlan",)
    fields = ("name", "vlan",)


class VolumeGroupAdmin(admin.ModelAdmin):
    list_display = ("id", "display_name", "type", "service",)
    fields = ("display_name", "type", "service",)


class VolumeGroupFileSystemAdmin(admin.ModelAdmin):
    list_display = ("id", "volume_group", "mount_path", "size",)
    fields = ("volume_group", "mount_path", "size",)


class VolumeAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "dpg", "datastore", "volume_group", "volume_type", "wwn", "display_name", "size", "status",
                    "instance_host",
                    "migration_state", "encryption_state", "order_tracking", "comment",)
    fields = (
        "dpg", "datastore", "volume_group", "volume_type", "wwn", "display_name", "size", "status",
        "instance_host",
        "migration_state", "encryption_state", "order_tracking", "comment",)


admin.site.register(ClusterAvailabilityLevel, ClusterAvailabilityLevelAdmin)
admin.site.register(ClusterCpuOversubscription, ClusterCpuOversubscriptionAdmin)
admin.site.register(ClusterMemoryOversubscription, ClusterMemoryOversubscriptionAdmin)
admin.site.register(CpuArchitecture, CpuArchitectureAdmin)
admin.site.register(CustomRamAnge, CustomRamAngeAdmin)
admin.site.register(DatabaseType, DatabaseTypeAdmin)
admin.site.register(DisasterRecoveryTenancy, DisasterRecoveryTenancyAdmin)
admin.site.register(EncryptionState, EncryptionStateAdmin)
admin.site.register(EsxHostCpuOversubscription, EsxHostCpuOversubscriptionAdmin)
admin.site.register(EsxHostMemoryOversubscription, EsxHostMemoryOversubscriptionAdmin)
admin.site.register(EventCategory, EventCategoryAdmin)
admin.site.register(EventOrigin, EventOriginAdmin)
admin.site.register(Eventource, EventourceAdmin)
admin.site.register(Eventtatus, EventtatusAdmin)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(HostState, HostStateAdmin)
admin.site.register(Hp3parTier, Hp3parTierAdmin)
admin.site.register(IpAddressAllocationState, IpAddressAllocationStateAdmin)
admin.site.register(IpAddressAllocationPurpose, IpAddressAllocationPurposeAdmin)
admin.site.register(LamaTemplateState, LamaTemplateStateAdmin)
admin.site.register(LamaTemplateStatus, LamaTemplateStatusAdmin)
admin.site.register(LicenseEventType, LicenseEventTypeAdmin)
admin.site.register(LifecycleActionType, LifecycleActionTypeAdmin)
admin.site.register(LifecycleState, LifecycleStateAdmin)
admin.site.register(LvmLevel, LvmLevelAdmin)
admin.site.register(LvmType, LvmTypeAdmin)
admin.site.register(MacAddressAllocationState, MacAddressAllocationStateAdmin)
admin.site.register(MigrationState, MigrationStateAdmin)
admin.site.register(SapOffering, SapOfferingAdmin)
admin.site.register(ServiceLevel, ServiceLevelAdmin)
admin.site.register(ServiceRole, ServiceRoleAdmin)
admin.site.register(SidOrigin, SidOriginAdmin)
admin.site.register(SidType, SidTypeAdmin)
admin.site.register(StorageStatus, StorageStatusAdmin)
admin.site.register(StorageType, StorageTypeAdmin)
admin.site.register(StorageWorkloadType, StorageWorkloadTypeAdmin)
admin.site.register(SubscriptionStatus, SubscriptionStatusAdmin)
admin.site.register(Suitability, SuitabilityAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(TicketClosureCodeInterpretation, TicketClosureCodeInterpretationAdmin)
admin.site.register(TicketImplementationStatus, TicketImplementationStatusAdmin)
admin.site.register(TicketOrigin, TicketOriginAdmin)
admin.site.register(Tickettate, TickettateAdmin)
admin.site.register(TicketType, TicketTypeAdmin)
admin.site.register(Topology, TopologyAdmin)
admin.site.register(Virtualization, VirtualizationAdmin)
admin.site.register(VlanRole, VlanRoleAdmin)
admin.site.register(VlanType, VlanTypeAdmin)
admin.site.register(VolumeGroupType, VolumeGroupTypeAdmin)
admin.site.register(VolumeType, VolumeTypeAdmin)
admin.site.register(WorkloadType, WorkloadTypeAdmin)
admin.site.register(Zone, ZoneAdmin)
admin.site.register(DataCenter, DataCenterAdmin)
admin.site.register(Vcenter, VcenterAdmin)
admin.site.register(Tenant, TenantAdmin)
admin.site.register(Cluster, ClusterAdmin)
admin.site.register(Hp3par, Hp3parAdmin)
admin.site.register(Cpg, CpgAdmin)
admin.site.register(CustomCpuValue, CustomCpuValueAdmin)
admin.site.register(Tier, TierAdmin)
admin.site.register(CustomSize, CustomSizeAdmin)
admin.site.register(Datastore, DatastoreAdmin)
admin.site.register(EsxHost, EsxHostAdmin)
admin.site.register(EventCode, EventCodeAdmin)
admin.site.register(Lvm, LvmAdmin)
admin.site.register(OrderTracking, OrderTrackingAdmin)
admin.site.register(System, SystemAdmin)
admin.site.register(TicketClosureCode, TicketClosureCodeAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Hp3parCapacity, Hp3parCapacityAdmin)
admin.site.register(Hp3parPair, Hp3parPairAdmin)
admin.site.register(OperatingSystem, OperatingSystemAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Vlan, VlanAdmin)
admin.site.register(InstanceHost, InstanceHostAdmin)
admin.site.register(NicType, NicTypeAdmin)
admin.site.register(IpAddressPool, IpAddressPoolAdmin)
admin.site.register(MacAddressPool, MacAddressPoolAdmin)
admin.site.register(InstanceHostNicConfig, InstanceHostNicConfigAdmin)
admin.site.register(LamaTemplateTargetSidInstanceHost, LamaTemplateTargetSidInstanceHostAdmin)
admin.site.register(LamaTemplateTargetSidInstanceHostNicConfig, LamaTemplateTargetSidInstanceHostNicConfigAdmin)
admin.site.register(LifecycleAction, LifecycleActionAdmin)
admin.site.register(LamaTemplate, LamaTemplateAdmin)
admin.site.register(LamaTemplateTargetSid, LamaTemplateTargetSidAdmin)
admin.site.register(ServiceRoleDetail, ServiceRoleDetailAdmin)
admin.site.register(LamaTemplateTargetSidService, LamaTemplateTargetSidServiceAdmin)
admin.site.register(LamaTemplateTargetSidVolume, LamaTemplateTargetSidVolumeAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Service_vip, Service_vipAdmin)
admin.site.register(SidLvmLicenseEvent, SidLvmLicenseEventAdmin)
admin.site.register(TenantUserGroup, TenantUserGroupAdmin)
admin.site.register(VlanTriplet, VlanTripletAdmin)
admin.site.register(Vla, VlaAdmin)
admin.site.register(Vmnetwork, VmnetworkAdmin)
admin.site.register(VolumeGroup, VolumeGroupAdmin)
admin.site.register(VolumeGroupFileSystem, VolumeGroupFileSystemAdmin)
admin.site.register(Volume, VolumeAdmin)

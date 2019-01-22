# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models


# Create your models here.

class ClusterAvailabilityLevel(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(ClusterAvailabilityLevel, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'cluster_availability_level'
        verbose_name = 'Cluster availability levels'
        verbose_name_plural = 'Cluster availability levels'


class ClusterCpuOversubscription(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(ClusterCpuOversubscription, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'cluster_cpu_oversubscription'
        verbose_name = 'Cluster cpu oversubscription'
        verbose_name_plural = 'Cluster cpu oversubscriptions'


class ClusterMemoryOversubscription(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(ClusterMemoryOversubscription, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'cluster_memory_oversubscription'
        verbose_name = 'cluster memory oversubscription'
        verbose_name_plural = 'Cluster memory oversubscriptions'


class CpuArchitecture(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(CpuArchitecture, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    cores = models.IntegerField(verbose_name='Cores')
    threads = models.IntegerField(verbose_name='Threads')
    max_hana_prod_vms_per_socket = models.IntegerField(verbose_name='Max hana prod vms per socket')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'cpu_architecture'
        verbose_name = 'Cpu architecture'
        verbose_name_plural = 'Cpu architectures'


class CustomRamAnge(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(CustomRamAnge, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    ram_start = models.IntegerField(verbose_name='Ram start')
    ram_end = models.IntegerField(verbose_name='Ram end')
    steps = models.IntegerField(verbose_name="Steps")
    unit = models.CharField(max_length=20, verbose_name='Unit')

    def __unicode__(self):
        return str(self.ram_start) + '-' + str(self.ram_end) + self.unit

    class Meta:
        db_table = 'custom_ram_range'
        verbose_name = 'Custom ram range'
        verbose_name_plural = 'Custom ram ranges'


class DatabaseType(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(DatabaseType, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'database_type'
        verbose_name = 'Database type'
        verbose_name_plural = 'Database types'


class DisasterRecoveryTenancy(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(DisasterRecoveryTenancy, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'disaster_recovery_tenancy'
        verbose_name = 'Disaster recovery tenancy'
        verbose_name_plural = 'Disaster recovery tenancys'


class EncryptionState(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(EncryptionState, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'encryption_state'
        verbose_name = 'Encryption state'
        verbose_name_plural = 'Encryption states'


class EsxHostCpuOversubscription(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(EsxHostCpuOversubscription, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'esx_host_cpu_oversubscription'
        verbose_name = 'Esx host cpu oversubscription'
        verbose_name_plural = 'Esx host cpu oversubscriptions'


class EsxHostMemoryOversubscription(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(EsxHostMemoryOversubscription, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'esx_host_memory_oversubscription'
        verbose_name = 'Esx host memory oversubscriptions'
        verbose_name_plural = 'Esx host memory oversubscriptions'


class EventCategory(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(EventCategory, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'event_category'
        verbose_name = 'Event category'
        verbose_name_plural = 'Event categorys'


class EventOrigin(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(EventOrigin, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'event_origin'
        verbose_name = 'Event origin'
        verbose_name_plural = 'Event origins'


class Eventource(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Eventource, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'event_source'
        verbose_name = 'Event source'
        verbose_name_plural = 'Event sources'


class Eventtatus(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Eventtatus, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'event_status'
        verbose_name = 'Event status'
        verbose_name_plural = 'Event statuss'


class EventType(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(EventType, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'event_type'
        verbose_name = 'Event type'
        verbose_name_plural = 'Event types'


class HostState(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(HostState, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'host_state'
        verbose_name = 'Host state'
        verbose_name_plural = 'Host states'


class Hp3parTier(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Hp3parTier, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'hp3par_tier'
        verbose_name = 'Hp3par tier'
        verbose_name_plural = 'Hp3par Tier'


class IpAddressAllocationState(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(IpAddressAllocationState, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    allocation_state = models.CharField(max_length=100, verbose_name='Allocation state')
    value = models.CharField(max_length=50, verbose_name="Value")

    def __unicode__(self):
        return self.allocation_state

    class Meta:
        db_table = 'ip_address_allocation_state'
        verbose_name = 'Ip address allocation state'
        verbose_name_plural = 'Ip address allocation states'


class IpAddressAllocationPurpose(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(IpAddressAllocationPurpose, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    allocation_purpose = models.CharField(max_length=100, verbose_name='Allocation purpose')
    value = models.CharField(max_length=50, verbose_name='Value')

    def __unicode__(self):
        return self.allocation_purpose

    class Meta:
        db_table = 'ipaddress_allocation_purpose'
        verbose_name = 'Ipaddress allocation purpose'
        verbose_name_plural = 'Ipaddress allocation purposes'


class LamaTemplateState(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(LamaTemplateState, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'lama_template_state'
        verbose_name = 'Lama template state'
        verbose_name_plural = 'Lama template states'


class LamaTemplateStatus(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(LamaTemplateStatus, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'lama_template_status'
        verbose_name = 'Lama template status'
        verbose_name_plural = 'Lama template statuss'


class LicenseEventType(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(LicenseEventType, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'license_event_type'
        verbose_name = 'License event type'
        verbose_name_plural = 'License event types'


class LifecycleActionType(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(LifecycleActionType, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'lifecycle_action_type'
        verbose_name = 'Lifecycle action type'
        verbose_name_plural = 'Lifecycle action types'


class LifecycleState(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(LifecycleState, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'lifecycle_state'
        verbose_name = 'Lifecycle state'
        verbose_name_plural = 'Lifecycle states'


class LvmLevel(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(LvmLevel, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'lvm_level'
        verbose_name = 'Lvm level'
        verbose_name_plural = 'Lvm levels'


class LvmType(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(LvmType, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'lvm_type'
        verbose_name = 'Lvm type'
        verbose_name_plural = 'Lvm types'


class MacAddressAllocationState(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(MacAddressAllocationState, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'mac_address_allocation_state'
        verbose_name = 'Mac address allocation state'
        verbose_name_plural = 'Mac address allocation states'


class MigrationState(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(MigrationState, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'migration_state'
        verbose_name = 'Migration state'
        verbose_name_plural = 'Migration states'


class SapOffering(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(SapOffering, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'sap_offering'
        verbose_name = 'Sap offering'
        verbose_name_plural = 'Sap offerings'


class ServiceLevel(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(ServiceLevel, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'service_level'
        verbose_name = 'Service level'
        verbose_name_plural = 'Service levels'


class ServiceRole(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(ServiceRole, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'service_role'
        verbose_name = 'Service role'
        verbose_name_plural = 'Service roles'


class SidOrigin(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(SidOrigin, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'sid_origin'
        verbose_name = 'Sid origin'
        verbose_name_plural = 'Sid origins'


class SidType(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(SidType, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'sid_type'
        verbose_name = 'Sid type'
        verbose_name_plural = 'Sid types'


class StorageStatus(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(StorageStatus, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'storage_status'
        verbose_name = 'Storage status'
        verbose_name_plural = 'Storage statuss'


class StorageType(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(StorageType, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')
    store_type_logo = models.CharField(max_length=50, verbose_name="Store type logo")

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'storage_type'
        verbose_name = 'Storage type'
        verbose_name_plural = 'Storage types'


class StorageWorkloadType(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(StorageWorkloadType, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    max_num_of_prod_inst_hosts = models.IntegerField(verbose_name='Max num of prod inst hosts')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'storage_workload_type'
        verbose_name = 'Storage workload type'
        verbose_name_plural = 'Storage workload types'


class SubscriptionStatus(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(SubscriptionStatus, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'subscription_status'
        verbose_name = 'Subscription status'
        verbose_name_plural = 'Subscription statuss'


class Suitability(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Suitability, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'suitability'
        verbose_name = 'Suitability'
        verbose_name_plural = 'SuitabilityS'


class Supplier(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Supplier, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'supplier'
        verbose_name = 'Supplier'
        verbose_name_plural = 'SupplierS'


class TicketClosureCodeInterpretation(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(TicketClosureCodeInterpretation, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'ticket_closure_code_interpretation'
        verbose_name = 'Ticket closure code interpretation'
        verbose_name_plural = 'Ticket closure code interpretations'


class TicketImplementationStatus(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(TicketImplementationStatus, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'ticket_implementation_status'
        verbose_name = 'Ticket implementation status'
        verbose_name_plural = 'Ticket implementation statuss'


class TicketOrigin(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(TicketOrigin, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'ticket_origin'
        verbose_name = 'Ticket origin'
        verbose_name_plural = 'Ticket origins'


class Tickettate(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Tickettate, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'ticket_state'
        verbose_name = 'Ticket state'
        verbose_name_plural = 'Ticket states'


class TicketType(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(TicketType, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'ticket_type'
        verbose_name = 'Ticket type'
        verbose_name_plural = 'Ticket types'


class Topology(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Topology, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'topology'
        verbose_name = 'Topology'
        verbose_name_plural = 'Topologys'


class Virtualization(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Virtualization, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'virtualization'
        verbose_name = 'Virtualization'
        verbose_name_plural = 'Virtualizations'


class VlanRole(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(VlanRole, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'vlan_role'
        verbose_name = 'Vlan role'
        verbose_name_plural = 'Vlan roles'


class VlanType(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(VlanType, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'vlan_type'
        verbose_name = 'Vlan type'
        verbose_name_plural = 'Vlan types'


class VolumeGroupType(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(VolumeGroupType, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'volume_group_type'
        verbose_name = 'Volume group types'
        verbose_name_plural = 'Volume group types'


class VolumeType(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(VolumeType, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'volume_type'
        verbose_name = 'Volume type'
        verbose_name_plural = 'Volume types'


class WorkloadType(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(WorkloadType, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'workload_type'
        verbose_name = 'Workload type'
        verbose_name_plural = 'Workload types'


class Zone(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Zone, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'zone'
        verbose_name = 'Zone'
        verbose_name_plural = 'Zones'


class DataCenter(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(DataCenter, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    legacy_vpc_name = models.CharField(max_length=20, verbose_name='Legacy vpc name')
    display_name = models.CharField(max_length=20, verbose_name='Display name')
    region = models.CharField(max_length=100, verbose_name='Region')
    country_code = models.CharField(max_length=20, verbose_name='Country code')
    timezone = models.CharField(max_length=20, verbose_name='Timezone')
    dual_dc_pair = models.BooleanField(verbose_name='Dual dc pair')
    secondary_site = models.BooleanField(verbose_name='Secondary site ')
    # paired_datacenter = models.ForeignKey(DataCenter,verbose_name='Paired datacenter')
    pci_enabled = models.BooleanField(verbose_name='Pci enabled')
    disaster_recovery_enabled = models.BooleanField(verbose_name='Disaster recovery enabled')
    disaster_recovery_site_name = models.CharField(max_length=100, verbose_name='Disaster recovery site name')
    country = models.CharField(max_length=100, verbose_name='Country')
    iso_3166_01_code = models.CharField(max_length=100, verbose_name='Iso 3166 01 code')
    location_currency_code = models.CharField(max_length=100, verbose_name='Location currency code')
    location_currency_symbol = models.CharField(max_length=100, verbose_name='Location currency symbol')
    location = models.CharField(max_length=100, verbose_name='Location')
    service_delivery_manager_name = models.CharField(max_length=100, verbose_name='Service delivery manager name')
    service_delivery_manager_email = models.EmailField(verbose_name='Service delivery manager email ')
    site_technical_coordinator_name = models.CharField(max_length=100, verbose_name='Site technical coordinator name')
    site_technical_coordinator_email = models.EmailField(verbose_name='Site technical coordinator email')
    provisioning_coordinator_name = models.CharField(max_length=100, verbose_name='Provisioning coordinator name')
    provisioning_coordinator_email = models.EmailField(verbose_name='Provisioning coordinator email')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'data_center'
        verbose_name = 'Data center'
        verbose_name_plural = 'Data centers'


class Vcenter(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Vcenter, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    name = models.CharField(max_length=50, verbose_name='Name')
    host = models.CharField(max_length=50, verbose_name='Host')
    ip = models.CharField(max_length=50, verbose_name='Ip')
    username = models.CharField(max_length=50, verbose_name='Username')
    password = models.CharField(max_length=50, verbose_name='Password')
    port = models.IntegerField(verbose_name='Port')
    vmware_dc = models.CharField(max_length=50, verbose_name='Vmware_dc')
    datacenter = models.ForeignKey(DataCenter, verbose_name='Datacenter')
    zone = models.ForeignKey(Zone, verbose_name='Zone')
    lfecycle_state = models.ForeignKey(LifecycleState, verbose_name='Lifecycle_state')
    asser_tag = models.CharField(max_length=100, verbose_name='Asser_tag')
    capacity_team_model_name = models.CharField(max_length=100, verbose_name='Capacity_team_model_name')
    capacity_team_device_registration_name = models.CharField(max_length=100,
                                                              verbose_name='Capacity_team_device_registration_name')
    annotation = models.TextField(verbose_name='Annotation')

    def __unicode__(self):
        return self.host

    class Meta:
        db_table = 'vcenter'
        verbose_name = 'Vcenter'
        verbose_name_plural = 'Vcenters'


class Tenant(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Tenant, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    COLORS = (
        ('send_nothing', 'send_nothing'),
        ('send_email', 'send_email'),
        ('send_ticket', 'send_ticket'),
    )
    datacenter = models.ForeignKey(DataCenter, verbose_name="Datacenter")
    name = models.CharField(max_length=50, verbose_name="Name")
    display_name = models.CharField(max_length=50, verbose_name="Display name")
    esl_customer_name = models.CharField(max_length=50, verbose_name="Esl customer name")
    esl_company_id = models.CharField(max_length=50, verbose_name="Esl company id")
    company_id_for_storage_naming = models.CharField(max_length=50, verbose_name="Company id for storage naming")
    email_distribution = models.CharField(max_length=100, verbose_name="Email distribution")
    hmco_action = models.CharField(max_length=50, choices=COLORS, verbose_name="Hmco action")
    sidType = models.ManyToManyField(SidType, verbose_name='SidType')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'tenant'
        verbose_name = 'Tenant'
        verbose_name_plural = 'Tenants'


class Cluster(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Cluster, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    name = models.CharField(max_length=50, verbose_name='Name')
    vcenter = models.ForeignKey(Vcenter, verbose_name='Vcenter')
    data_center = models.ForeignKey(DataCenter, verbose_name='Data center')
    tenant = models.ManyToManyField(Tenant, verbose_name='Tenant')
    serviceLevel = models.ManyToManyField(ServiceLevel, verbose_name='ServiceLevel')
    lifecycle_state = models.ForeignKey(LifecycleState, verbose_name='Lifecycle state')
    cpu_oversubscription = models.ForeignKey(ClusterCpuOversubscription, verbose_name='Cpu oversubscription')
    warn_cpu_oversubscription_pct = models.IntegerField(verbose_name='Warn cpu oversubscription pct')
    alert_cpu_oversubscription_pct = models.IntegerField(verbose_name='Alert cpu oversubscription pct')
    lca_cpu_oversubscription_pct = models.IntegerField(verbose_name='Lca cpu oversubscription pct')
    make_unavailable_cpu_oversubscription_pct = models.IntegerField(
        verbose_name='Make unavailable cpu oversubscription pct')
    last_known_cpu_oversubscription_pct = models.IntegerField(verbose_name='Last known cpu oversubscription pct')
    memory_oversubscription = models.ForeignKey(ClusterMemoryOversubscription,
                                                verbose_name='Memory oversubscription')
    warn_memory_oversubscription_pct = models.IntegerField(verbose_name='Warn memory oversubscription pct')
    alert_memory_oversubscription_pct = models.IntegerField(verbose_name='Alert memory oversubscription pct')
    lca_memory_oversubscription_pct = models.IntegerField(verbose_name='Lca memory oversubscription pct')
    make_unavailable_memory_oversubscription_pct = models.IntegerField(
        verbose_name='Make unavailable memory oversubscription pct')
    last_known_memory_oversubscription_pct = models.IntegerField(verbose_name='Last known memory oversubscription pct')
    max_num_of_rdm = models.IntegerField(verbose_name='Max num of rdm')
    warn_rdm_oversubscription_pct = models.IntegerField(verbose_name='Warn rdm oversubscription pct')
    alert_rdm_oversubscription_pct = models.IntegerField(verbose_name='Alert rdm oversubscription pct')
    lca_rdm_oversubscription_pct = models.IntegerField(verbose_name='Lca rdm oversubscription pct')
    make_unavailable_rdm_oversubscription_pct = models.IntegerField(
        verbose_name='Make unavailable rdm oversubscription pct')
    last_known_num_of_rdm = models.IntegerField(verbose_name='Last known num of rdm')
    asset_tag = models.CharField(max_length=200, verbose_name='Asset tag')
    capacity_team_model_name = models.CharField(max_length=200, verbose_name='Capacity team model name')
    capacity_team_device_registration_name = models.CharField(max_length=200,
                                                              verbose_name='Capacity team device registration name')
    manual_override = models.BooleanField(verbose_name='Manual override')
    annotation = models.TextField(verbose_name='Annotation')
    last_updated_on = models.DateTimeField(verbose_name='Last updated on')

    def __unicode__(self):
        pass

    class Meta:
        db_table = 'cluster'
        verbose_name = 'Cluster'
        verbose_name_plural = 'Clusters'


class Hp3par(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Hp3par, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    name = models.CharField(max_length=100, verbose_name='Name')
    zone = models.ForeignKey(Zone, verbose_name='Zone')
    storageworkload = models.ForeignKey(StorageWorkloadType, verbose_name='Storageworkload')
    ip = models.CharField(max_length=100, verbose_name='Ip')
    url = models.URLField(verbose_name='Url')
    username = models.CharField(max_length=50, verbose_name='Username')
    password = models.CharField(max_length=50, verbose_name='Password')
    datacenter = models.ForeignKey(DataCenter, verbose_name='Datacenter')
    lifecycle_state = models.ForeignKey(LifecycleState, verbose_name='Lifecycle state')
    asset_tag = models.CharField(max_length=100, verbose_name='Asset tag')
    capacity_team_model_name = models.CharField(max_length=100, verbose_name='Capacity team model name')
    capacity_tea_device_registration_name = models.CharField(max_length=100,
                                                             verbose_name='Capacity tea device registration name')
    manual_override = models.BooleanField(verbose_name='Manual override')
    annotation = models.TextField(verbose_name='Annotation')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'hp3par'
        verbose_name = 'Hp3par'
        verbose_name_plural = 'Hp3pars'


class Cpg(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Cpg, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    name = models.CharField(max_length=50, verbose_name='Name')
    display_name = models.CharField(max_length=50, verbose_name='Display name')
    type = models.ForeignKey(StorageType, verbose_name='Type')
    domain = models.CharField(max_length=50, verbose_name='Domain')
    the_volume_set_must_be_used = models.BooleanField(verbose_name='The volume set must be used')
    dedicated_to_a_tenant = models.BooleanField(verbose_name='Dedicated to a tenant')
    virtual_volume_set = models.CharField(max_length=100, verbose_name='Virtual volume set')
    highly_available = models.BooleanField(verbose_name='Highly available')
    dr_replication = models.BooleanField(verbose_name='Dr replication')

    hp3par = models.ForeignKey(Hp3par, verbose_name='Hp3par')
    tenant = models.ForeignKey(Tenant, verbose_name='Tenant')

    def __unicode__(self):
        return self.hp3par.name + '->' + self.name

    class Meta:
        db_table = 'cpg'
        verbose_name = 'Cpg'
        verbose_name_plural = 'Cpgs'


class CustomCpuValue(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(CustomCpuValue, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    cpuarchitecture = models.ForeignKey(CpuArchitecture, verbose_name='Cpuarchitecture')
    vcpu = models.IntegerField(verbose_name='Vcpu')
    socket = models.IntegerField(verbose_name='Socket')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'custom_cpu_value'
        verbose_name = 'Custom cpu value'
        verbose_name_plural = 'Custom cpu values'


class Tier(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Tier, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    name = models.CharField(max_length=50, verbose_name='Name')
    workloads = models.ManyToManyField(WorkloadType, verbose_name='Workloads')
    suitabilities = models.ManyToManyField(Suitability, verbose_name='Suitabilities')
    description = models.CharField(max_length=100, verbose_name='Description')
    cluster = models.ManyToManyField(Cluster, verbose_name='Cluster')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Tier'
        verbose_name = 'Tier'
        verbose_name_plural = 'Tiers'


class CustomSize(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(CustomSize, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    tier = models.ForeignKey(Tier, verbose_name='Tier')
    tenant = models.ManyToManyField(Tenant, verbose_name='Tenant')
    customcpuvalue = models.ForeignKey(CustomCpuValue, verbose_name='Customcpuvalue')
    customramrange = models.ForeignKey(CustomRamAnge, verbose_name='Customramrange')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'CustomSize'
        verbose_name = 'Custom size'
        verbose_name_plural = 'Custom Size'


class Datastore(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Datastore, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=50, verbose_name='Display name')
    name = models.CharField(max_length=50, verbose_name='')
    storage_type = models.ForeignKey(StorageType, verbose_name='Storage type')
    cluster = models.ForeignKey(Cluster, verbose_name='Cluster')
    dr_replication = models.BooleanField(verbose_name='Dr replication')
    dedicated_to_a_tenant = models.BooleanField(verbose_name='Dedicated to a tenant')
    tenant = models.ManyToManyField(Tenant, verbose_name='Tenant')
    lifecycle_state = models.ForeignKey(LifecycleState, verbose_name='Lifecycle_state')
    total_capacity = models.BooleanField(verbose_name='Total capacity')
    reserved_capacity = models.IntegerField(verbose_name='Reserved capacity')
    warn_pct = models.IntegerField(verbose_name='Warn pct')
    alert_pct = models.IntegerField(verbose_name='Alert pct')
    lca_pct = models.IntegerField(verbose_name='Lca pct')
    make_unavailable_pct = models.IntegerField(verbose_name='Make unavailable pct')
    last_known_oversubscription_pct = models.IntegerField(verbose_name='Last known oversubscription pct')
    warn_vmdk_pct = models.IntegerField(verbose_name='Warn vmdk pct')
    alert_vmdk_pct = models.IntegerField(verbose_name='Alert vmdk pct')
    lca_vmdk_pct = models.IntegerField(verbose_name='Lca vmdk pct')
    make_unavailable_vmdk_pct = models.IntegerField(verbose_name='Make unavailable vmdk pct')
    last_known_vmdk_pct = models.IntegerField(verbose_name='Last known vmdk pct')
    manual_override = models.BooleanField(verbose_name='Manual override')
    last_updated_on = models.DateTimeField(verbose_name='Last updated on')

    def __unicode__(self):
        pass

    class Meta:
        db_table = 'datastore'
        verbose_name = 'Datastore'
        verbose_name_plural = 'Datastores'


class EsxHost(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(EsxHost, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    cluster = models.ForeignKey(Cluster, verbose_name='Cluster')
    cpuarchitecture = models.ForeignKey(CpuArchitecture, verbose_name='Cpuarchitecture')
    fqdn = models.CharField(max_length=100, verbose_name='Fqdn')
    socket = models.IntegerField(verbose_name='Socket')
    hyperthreading = models.BooleanField(verbose_name='Hyperthreading')
    ram = models.IntegerField(verbose_name='Ram')
    lifecycle_state = models.ForeignKey(LifecycleState, verbose_name='Lifecycle_state')
    asset_tag = models.CharField(max_length=100, verbose_name='Asset tag')
    capacity_team_model_name = models.CharField(max_length=100, verbose_name='Capacity team model name')
    capacity_team_device_registration_name = models.CharField(max_length=100,
                                                              verbose_name='Capacity team device registration name')
    annotation = models.TextField(verbose_name='Annotation')

    def __unicode__(self):
        return self.fqdn

    class Meta:
        db_table = 'esx_host'
        verbose_name = 'Esx host'
        verbose_name_plural = 'Esx Hosts'


class EventCode(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(EventCode, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    template = models.TextField(verbose_name='Template')
    supplier = models.ForeignKey(Supplier, verbose_name='Supplier')
    type = models.ForeignKey(EventType, verbose_name='Type')
    category = models.ForeignKey(EventCategory, verbose_name='Category')
    source = models.ForeignKey(Eventource, verbose_name='Source')
    origin = models.ForeignKey(EventOrigin, verbose_name='Origin')
    reference_code = models.CharField(max_length=100, verbose_name='Reference code')
    summary = models.CharField(max_length=100, verbose_name='Summary')
    description = models.TextField(verbose_name='Description')
    annotation = models.TextField(verbose_name='Annotation')

    def __unicode__(self):
        return self.reference_code

    class Meta:
        db_table = 'event_code'
        verbose_name = 'Event code'
        verbose_name_plural = 'Event codes'


class Lvm(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Lvm, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    name = models.CharField(max_length=50, verbose_name='Name')
    type = models.ForeignKey(LvmType, verbose_name='Type')
    lvm_host = models.CharField(max_length=50, verbose_name='Lvm host')
    lvm_username = models.CharField(max_length=50, verbose_name='Lvm password')
    lvm_password = models.CharField(max_length=50, verbose_name='Lvm password')
    lvm_url = models.URLField(verbose_name='Lvm url')
    datacenter = models.ForeignKey(DataCenter, verbose_name='Datacenter')
    lifecycle_state = models.ForeignKey(LifecycleState, verbose_name='Lifecycle state')

    def __unicode__(self):
        return self.lvm_host

    class Meta:
        db_table = 'lvm'
        verbose_name = 'Lvm'
        verbose_name_plural = 'Lvms'


class OrderTracking(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(OrderTracking, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    tenant = models.ForeignKey(Tenant, verbose_name='Tenant')
    product_uuid = models.CharField(max_length=50, verbose_name='Product uuid')
    product_name = models.CharField(max_length=50, verbose_name='Product name')
    order_id = models.CharField(max_length=50, verbose_name='Order id')
    order_uuid = models.CharField(max_length=50, verbose_name='Order uuid')
    supplier_request_id = models.CharField(max_length=50, verbose_name='Supplier request id')
    order_item_id = models.CharField(max_length=50, verbose_name='Order item id')
    subscription_uuid = models.CharField(max_length=50, verbose_name='Subscription uuid')
    subscription_instance_component_uuid = models.CharField(max_length=50,
                                                            verbose_name='Subscription instance component uuid')
    subscription_owner_id = models.CharField(max_length=50, verbose_name='Subscription owner id')

    def __unicode__(self):
        return self.tenant.display_name + str(self.id)

    class Meta:
        db_table = 'order_tracking'
        verbose_name = 'Order tracking'
        verbose_name_plural = 'Order trackings'


class System(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(System, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    datacenter = models.ForeignKey(DataCenter, verbose_name='Datacenter')
    lvm_host = models.ForeignKey(Lvm, related_name='System_lvm_host', verbose_name='Lvm host')
    lama_host = models.ForeignKey(Lvm, related_name='System_lama_host', verbose_name='Lama host')
    sap_sid = models.CharField(max_length=20, verbose_name='Sap sid')
    primary_system = models.ForeignKey(SidOrigin, verbose_name='Primary system')
    # source = models.CharField(System,verbose_name='Source')
    lvm_serviceid = models.CharField(max_length=100, verbose_name='Lvm serviceid')
    tenant = models.ForeignKey(Tenant, verbose_name='Tenant')
    subscription_status = models.ForeignKey(SubscriptionStatus, verbose_name='Subscription status')
    backup_enabled = models.BooleanField(verbose_name='Backup enabled')
    highly_available = models.BooleanField(verbose_name='Highly available')
    service_level = models.ForeignKey(ServiceLevel, verbose_name='Service level')
    eu_data_privacy_support = models.BooleanField(verbose_name='Eu data privacy support')
    disaster_recovery_enabled = models.BooleanField(verbose_name='Disaster recovery enabled')
    disaster_recovery_infrastructure_tenancy_preference = models.ForeignKey(DisasterRecoveryTenancy,
                                                                            verbose_name='Disaster recovery infrastructure tenancy preference')
    lvm_level = models.ForeignKey(LvmLevel, verbose_name='Lvm level')
    hana_configuration = models.BooleanField(verbose_name='Hana configuration')
    database_type = models.ForeignKey(DatabaseType, verbose_name='Database type')
    sid_type = models.ForeignKey(SidType, verbose_name='Sid type')
    workload_type = models.ForeignKey(WorkloadType, verbose_name='Workload type')
    sap_offering = models.ForeignKey(SapOffering, verbose_name='Sap offering')
    order_tracking = models.ForeignKey(OrderTracking, verbose_name='Order tracking')
    migration_state = models.ForeignKey(MigrationState, verbose_name='Migration state')

    def __unicode__(self):
        pass

    class Meta:
        db_table = 'system'
        verbose_name = 'System'
        verbose_name_plural = 'Systems'


class TicketClosureCode(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(TicketClosureCode, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')
    interpretation = models.ForeignKey(TicketClosureCodeInterpretation, verbose_name='Interpretation')
    test_mode = models.BooleanField(verbose_name='Test mode')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'ticket_closure_code'
        verbose_name = 'Ticket closure code'
        verbose_name_plural = 'Ticket closure codes'


class Ticket(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Ticket, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    COLORS_Billable = (
        ('Unknown', 'Unknown'),
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    COLORS_Emergency_change = COLORS_Billable
    COLORS_Category = (
        ('HMCO', 'HMCO'),
        ('DR', 'DR'),
        ('EAO', 'EAO'),
        ('DB_STORAGE', 'DB_STORAGE'),
        ('CS_STORAGE', 'CS_STORAGE'),
        ('PAS_STORAGE', 'PAS_STORAGE'),
    )
    sm9_endpoint = models.CharField(max_length=50, verbose_name='Sm9 endpoint')
    billable = models.CharField(max_length=15, choices=COLORS_Billable, verbose_name='Billable')
    company_id = models.CharField(max_length=10, verbose_name='Company id')
    location_id = models.CharField(max_length=10, verbose_name='Management region')
    management_region = models.CharField(max_length=50, verbose_name='Management region')
    user_id = models.CharField(max_length=100, verbose_name='User id')
    emergency_change = models.CharField(max_length=15, choices=COLORS_Emergency_change, verbose_name='Emergency change')
    ticket_id = models.CharField(max_length=30, verbose_name='Ticket id')
    type = models.ForeignKey(TicketType, verbose_name='Type')
    origin = models.ForeignKey(TicketOrigin, verbose_name='Origin')
    order = models.ForeignKey(OrderTracking, verbose_name='Order')
    action_request_id = models.CharField(max_length=50, verbose_name='Action request id')
    category = models.CharField(max_length=15, choices=COLORS_Category, verbose_name='Category')
    last_known_state = models.ForeignKey(Tickettate, verbose_name='Last known state')
    closure_code = models.ForeignKey(TicketClosureCode, verbose_name='Closure code')
    implementation_status = models.ForeignKey(TicketImplementationStatus, verbose_name='Implementation status')
    created_on = models.DateTimeField(verbose_name='Created on')

    def __unicode__(self):
        return self.ticket_id

    class Meta:
        db_table = 'ticket'
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'


class Event(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Event, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    datacenter = models.ForeignKey(DataCenter, verbose_name='Datacenter')
    tenant = models.ForeignKey(Tenant, verbose_name='Tenant')
    username = models.CharField(max_length=50, verbose_name='Username')
    code = models.ForeignKey(EventCode, verbose_name='Code')
    status = models.ForeignKey(Eventtatus, verbose_name='Status')
    sid = models.ForeignKey(System, verbose_name='Sid')
    ticket = models.ForeignKey(Ticket, verbose_name='Ticket')
    # source_event = models.ForeignKey(Event,verbose_name='Source event')
    incident = models.CharField(max_length=50, verbose_name='Incident')
    message = models.TextField(verbose_name='Message')

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = 'event'
        verbose_name = 'Event'
        verbose_name_plural = 'Event'


class Hp3parCapacity(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Hp3parCapacity, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    hp3par = models.ForeignKey(Hp3par, verbose_name='Hp3par')
    tier = models.ForeignKey(Hp3parTier, verbose_name='Tier')
    total_capacity = models.IntegerField(verbose_name='Total capacity')
    reserved_capacity = models.IntegerField(verbose_name='Reserved capacity')
    free_capacity = models.IntegerField(verbose_name='Free capacity')
    warn_pct = models.IntegerField(verbose_name='Warn pct')
    alert_pct = models.IntegerField(verbose_name='Alert pct')
    lca_pct = models.IntegerField(verbose_name='Lca pct')
    make_unavailable_pct = models.IntegerField(verbose_name='Make unavailable pct')
    warn_phy_pct = models.IntegerField(verbose_name='Warn phy pct')
    alert_phy_pct = models.IntegerField(verbose_name='Alert phy pct')
    lca_phy_pct = models.IntegerField(verbose_name='Lca phy pct')
    make_unavailable_phy_pct = models.IntegerField(verbose_name='Make unavailable phy pct')
    last_known_tier_oversubscription_pct = models.IntegerField(verbose_name='Last known tier oversubscription pct')
    last_known_tier_utilization_pct = models.IntegerField(verbose_name='Last known tier utilization pct')
    last_updated_on = models.DateTimeField(verbose_name='Last updated on')

    def __unicode__(self):
        return self.hp3par.display_name + '->' + self.tier.display_name

    class Meta:
        db_table = 'hp3par_capacity'
        verbose_name = 'Hp3par capacity'
        verbose_name_plural = 'Hp3par capacitys'


class Hp3parPair(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Hp3parPair, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    zone1_3par = models.ForeignKey(Hp3par, related_name='Hp3parPair_zone1_3par', verbose_name='Zone1 3par')
    zone2_3par = models.ForeignKey(Hp3par, related_name='Hp3parPair_zone2_3par', verbose_name='Zone2 3par')
    dr_partner_array_name = models.CharField(max_length=50, verbose_name='Dr partner array name')

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = 'hp3par_pair'
        verbose_name = 'Hp3par pair'
        verbose_name_plural = 'Hp3par pairs'


class OperatingSystem(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(OperatingSystem, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=100, verbose_name='Value')
    type = models.CharField(max_length=20, verbose_name='Type')
    virtualization = models.ForeignKey(Virtualization, verbose_name='Virtualization')
    username = models.CharField(max_length=20, verbose_name='Username')
    password = models.CharField(max_length=20, verbose_name='Password')
    goe_os_version = models.CharField(max_length=100, verbose_name='Goe os version')
    glance_id = models.CharField(max_length=50, verbose_name='Glance id')
    location = models.CharField(max_length=50, verbose_name='Location')

    def __unicode__(self):
        return self.virtualization.display_name + '->' + self.display_name

    class Meta:
        db_table = 'operating_system'
        verbose_name = 'Operating system'
        verbose_name_plural = 'Operating Systems'


class Image(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Image, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    name = models.CharField(max_length=100, verbose_name='Name')
    operatingSystem = models.ForeignKey(OperatingSystem, verbose_name='OperatingSystem')
    vcenter = models.ForeignKey(Vcenter, verbose_name='Vcenter')
    supported_for_hana = models.BooleanField(verbose_name='Supported for hana')

    def __unicode__(self):
        return self.vcenter.host + '-' + self.name

    class Meta:
        db_table = 'image'
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


class Size(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Size, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    cpu = models.IntegerField(verbose_name='Cpu')
    socket = models.IntegerField(verbose_name='SOcket')
    ram = models.IntegerField(verbose_name='Ram')
    system_disk = models.IntegerField(verbose_name='System disk')
    tenant = models.ManyToManyField(Tenant, verbose_name='Tenant')
    virtualization = models.ForeignKey(Virtualization, verbose_name='Virtualization')
    cpuarchitecture = models.ForeignKey(CpuArchitecture, verbose_name='Cpuarchitecture')
    lifecycle_state = models.ForeignKey(LifecycleState, verbose_name='Lifecycle state')
    tier = models.ForeignKey(Tier, verbose_name='Tier')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'size'
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'


class Vlan(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Vlan, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    vlanid = models.CharField(max_length=50, verbose_name='Vlanid')
    type = models.ForeignKey(VlanType, verbose_name='Type')
    role = models.ForeignKey(VlanRole, verbose_name='Role')
    only_for_eso4sap_use = models.BooleanField(verbose_name='Only for eso4sap use')
    netword = models.CharField(max_length=20, verbose_name='Netword')
    mask = models.CharField(max_length=20, verbose_name='Mask')
    gateway = models.CharField(max_length=20, verbose_name='Gateway')
    range_start = models.CharField(max_length=20, verbose_name='Range start')
    range_end = models.CharField(max_length=20, verbose_name='Range end')
    dns1 = models.CharField(max_length=20, verbose_name='Dns1')
    dns2 = models.CharField(max_length=20, verbose_name='Dns2')
    ntp = models.CharField(max_length=20, verbose_name='Ntp')
    byoip_enabled = models.BooleanField(verbose_name='Byoip_enabled')
    byoip_subnet = models.CharField(max_length=20, verbose_name='Byoip subnet')
    byoip_range_start = models.CharField(max_length=20, verbose_name='Byoip range start')
    byoip_range_end = models.CharField(max_length=20, verbose_name='Byoip range end')
    public_ip_enabled = models.BooleanField(verbose_name='Public ip enabled')
    public_ip_subnet = models.CharField(max_length=20, verbose_name='Public ip subnet')
    public_ip_range_start = models.CharField(max_length=20, verbose_name='Public ip range start')
    public_ip_range_end = models.CharField(max_length=20, verbose_name='Public ip range end')
    load_balance_enabled = models.BooleanField(verbose_name='Load balance enabled')
    tenant = models.ForeignKey(Tenant, verbose_name='Tenant')
    datacenter = models.ForeignKey(DataCenter, verbose_name='Datacenter')
    lifecycle_state = models.ForeignKey(LifecycleState, verbose_name='Lifecycle state')

    def __unicode__(self):
        pass

    class Meta:
        db_table = 'vlan'
        verbose_name = 'Vlan'
        verbose_name_plural = 'Vlans'


class InstanceHost(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(InstanceHost, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    hostname = models.CharField(max_length=100, verbose_name='Hostname')
    fqdn = models.CharField(max_length=100, verbose_name='Fqdn')
    cpuarchitecture = models.ForeignKey(CpuArchitecture, verbose_name='Cpuarchitecture')
    core = models.IntegerField(verbose_name='Core')
    socket = models.IntegerField(verbose_name='Socket')
    cpucount = models.IntegerField(verbose_name='Cpucount')
    memory = models.IntegerField(verbose_name='Memory')
    is_user_defined_size = models.BooleanField(verbose_name='Is user defined size')
    size = models.ForeignKey(Size, verbose_name='Size')
    operatingSystem = models.ForeignKey(OperatingSystem, verbose_name='OperatingSystem')
    saps = models.IntegerField(verbose_name='Saps')
    administrator_name = models.CharField(max_length=100, verbose_name='Administrator name')
    administrator_password = models.CharField(max_length=100, verbose_name='Administrator password')
    type = models.ForeignKey(Virtualization, verbose_name='Type')
    cluster = models.ForeignKey(Cluster, verbose_name='Cluster')
    esxhost = models.ForeignKey(EsxHost, verbose_name='Esxhost')
    datastore = models.ForeignKey(Datastore, verbose_name='Datastore')
    hp3par = models.ForeignKey(Hp3par, verbose_name='Hp3par')
    production_vlan = models.ForeignKey(Vlan, related_name='InstanceHost_Production_vlan',
                                        verbose_name='Production vlan')
    production_vlan_ip_address = models.CharField(max_length=100,
                                                  verbose_name='Production vlan ip address')
    fsr_vlan = models.ForeignKey(Vlan, related_name='InstanceHost_Hsr_vlan', verbose_name='Hsr vlan')
    hsr_vlan_ip_address = models.CharField(max_length=100, verbose_name='Hsr vlan ip address')
    internal_management_vlan = models.ForeignKey(Vlan, related_name='Internal_management_vlan',
                                                 verbose_name='Internal management vlan')
    internal_management_vlan_ip_address = models.CharField(max_length=100,
                                                           verbose_name='Internal management vlan ip address')
    state = models.ForeignKey(HostState, verbose_name='State')
    backup_enabled = models.BooleanField(verbose_name='Backup enabled')
    migration_state = models.ForeignKey(MigrationState, verbose_name='Migration state')
    encryption_state = models.ForeignKey(EncryptionState, verbose_name='Encryption state')
    order_tracking = models.ForeignKey(OrderTracking, verbose_name='Order tracking')
    suitability = models.ForeignKey(Suitability, verbose_name='Suitability')
    zone = models.ForeignKey(Zone, verbose_name='Zone')
    is_goe_provisioned = models.BooleanField(verbose_name='Is goe provisioned')

    def __unicode__(self):
        return self.hostname

    class Meta:
        db_table = 'instance_host'
        verbose_name = 'Instance host'
        verbose_name_plural = 'Instance hosts'


class NicType(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(NicType, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    nic_id = models.CharField(max_length=50, verbose_name='Nic id')
    vlan_role = models.ForeignKey(VlanRole, verbose_name='Vlan_role')

    def __unicode__(self):
        return self.nic_id

    class Meta:
        db_table = 'nic_type'
        verbose_name = 'Nic type'
        verbose_name_plural = 'Nic types'


class IpAddressPool(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(IpAddressPool, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    vlan = models.ForeignKey(Vlan, verbose_name='Vlan')
    ipv4_address = models.CharField(max_length=30, verbose_name='Ipv4 address')
    ipv6_address = models.CharField(max_length=30, verbose_name='Ipv6 address')
    hostname = models.CharField(max_length=50, verbose_name='Hostname')
    dns_suffix = models.CharField(max_length=50, verbose_name='Dns suffix')
    fqdn = models.CharField(max_length=50, verbose_name='Fqdn')
    allocation_purpose = models.ForeignKey(IpAddressAllocationPurpose, verbose_name='Allocation purpose')
    allocation_state = models.ForeignKey(IpAddressAllocationState, verbose_name='Allocation state')

    def __unicode__(self):
        return self.ipv4_address

    class Meta:
        db_table = 'ip_address_pool'
        verbose_name = 'Ip address pool'
        verbose_name_plural = 'Ip address pools'


class MacAddressPool(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(MacAddressPool, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    datacenter = models.ForeignKey(DataCenter, verbose_name='Datacenter')
    mac_address = models.CharField(max_length=50, verbose_name='Mac address')
    allocation_state = models.ForeignKey(MacAddressAllocationState, verbose_name='Allocation state')
    allocated_on = models.DateTimeField(verbose_name='Allocated on')

    def __unicode__(self):
        pass

    class Meta:
        db_table = 'mac_address_pool'
        verbose_name = 'Mac address pool'
        verbose_name_plural = 'Mac address pools'


class InstanceHostNicConfig(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(InstanceHostNicConfig, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    instancehost = models.ForeignKey(InstanceHost, verbose_name='Instancehost')
    nic_type = models.ForeignKey(NicType, verbose_name='Nic type')
    vlan = models.ForeignKey(Vlan, verbose_name='Vlan')
    ip_address = models.ForeignKey(IpAddressPool, verbose_name='Ip address')
    mac_address = models.ForeignKey(MacAddressPool, verbose_name='Mac address')

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = 'instance_host_nic_config'
        verbose_name = 'Instance host nic config'
        verbose_name_plural = 'Instance host nic configs'


class LamaTemplateTargetSidInstanceHost(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(LamaTemplateTargetSidInstanceHost, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    hostname = models.CharField(max_length=50, verbose_name='Hostname')
    fqdn = models.CharField(max_length=50, verbose_name='Fqdn')
    is_user_defined_size = models.BooleanField(verbose_name='Is user defined size')
    size = models.ForeignKey(Size, verbose_name='Size')
    socket = models.IntegerField(verbose_name='Socket')
    core = models.IntegerField(verbose_name='Core')
    cpuarchitecture = models.ForeignKey(CpuArchitecture, verbose_name='Cpuarchitecture')
    cpucount = models.IntegerField(verbose_name='Cpucount')
    memory = models.IntegerField(verbose_name='Memory')
    operatingSystem = models.ForeignKey(OperatingSystem, verbose_name='OperatingSystem')
    type = models.ForeignKey(Virtualization, verbose_name='Type')
    cluster = models.ForeignKey(Cluster, verbose_name='Cluster')
    datastore = models.ForeignKey(Datastore, verbose_name='Datastore')
    production_vlan = models.ForeignKey(Vlan, related_name='LamaTemplateTargetSidInstanceHost_production_vlan',
                                        verbose_name='Production vlan')
    production_vlan_ip_address = models.CharField(max_length=50, verbose_name='Production vlan ip address')
    hsr_vlan = models.ForeignKey(Vlan, related_name='LamaTemplateTargetSidInstanceHost_hsr_vlan',
                                 verbose_name='Hsr vlan')
    hsr_vlan_ip_address = models.CharField(max_length=50, verbose_name='Hsr vlan ip address')
    internal_management_vlan = models.ForeignKey(Vlan,
                                                 related_name='LamaTemplateTargetSidInstanceHost_Internal_management_vlan',
                                                 verbose_name='Internal management vlan')
    internal_management_vlan_ip_address = models.CharField(max_length=50,
                                                           verbose_name='Internal management vlan ip address')
    zone = models.ForeignKey(Zone, verbose_name='Zone')
    migration_state = models.ForeignKey(MigrationState, verbose_name='Migration state')
    encryption_state = models.ForeignKey(EncryptionState, verbose_name='Encryption state')

    def __unicode__(self):
        return self.hostname

    class Meta:
        db_table = 'lama_template_target_sid_instance_host'
        verbose_name = 'Lama template target sid instance host'
        verbose_name_plural = 'Lama template target sid instance hosts'


class LamaTemplateTargetSidInstanceHostNicConfig(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(LamaTemplateTargetSidInstanceHostNicConfig, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    instancehost = models.ForeignKey(LamaTemplateTargetSidInstanceHost, verbose_name="Instancehost")
    nic_type = models.ForeignKey(NicType, verbose_name="Nic type")
    vlan = models.ForeignKey(Vlan, verbose_name="Vlan")
    ip_address = models.ForeignKey(IpAddressPool, verbose_name="Ip address")
    mac_address = models.ForeignKey(MacAddressPool, verbose_name="Mac address")

    def __unicode__(self):
        pass

    class Meta:
        db_table = 'lama_template_target_sid_instance_host_nic_config'
        verbose_name = 'Lama template target sid instance host nic config'
        verbose_name_plural = 'Lama template target sid instance host nic configs'


class LifecycleAction(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(LifecycleAction, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    name = models.CharField(max_length=50, verbose_name="Name")
    type = models.ForeignKey(LifecycleActionType, verbose_name="Type")
    description = models.CharField(max_length=50, verbose_name="Description")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'lifecycle_action'
        verbose_name = 'Lifecycle actions'
        verbose_name_plural = 'Lifecycle actions'


class LamaTemplate(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(LamaTemplate, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    description = models.CharField(max_length=100, verbose_name='Description')
    action = models.ForeignKey(LifecycleAction, verbose_name='Action')
    lama = models.ForeignKey(Lvm, verbose_name='Lama')
    lama_template_name = models.CharField(max_length=50, verbose_name='Lama template name')
    lama_template_id = models.CharField(max_length=50, verbose_name='Lama template id')
    source_sid = models.ForeignKey(System, related_name='LamaTemplate_Source_sid', verbose_name='Source sid')
    refresh_using_sid = models.ForeignKey(System, related_name='LamaTemplate_refresh_using_sid',
                                          verbose_name='Refresh using sid')
    state = models.ForeignKey(LamaTemplateState, related_name='LamaTemplate_state', verbose_name='State')
    status = models.ForeignKey(LamaTemplateStatus, related_name='LamaTemplate_status', verbose_name='Status')
    request_description = models.TextField(verbose_name='Request description')
    author_annotation = models.TextField(verbose_name='Author annotation')

    def __unicode__(self):
        return self.lama.name + '->' + self.display_name

    class Meta:
        db_table = 'lama_template'
        verbose_name = 'Lama template'
        verbose_name_plural = 'Lama templates'


class LamaTemplateTargetSid(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(LamaTemplateTargetSid, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    template = models.ForeignKey(LamaTemplate, verbose_name="Template")
    display_name = models.CharField(max_length=20, verbose_name="Display name")
    primary_system = models.ForeignKey(SidOrigin, verbose_name="Primary system")
    datacenter = models.ForeignKey(DataCenter, verbose_name="Datacenter")
    tenant = models.ForeignKey(Tenant, verbose_name="Tenant")
    backup_enabled = models.BooleanField(verbose_name="Backup enabled")
    highly_available = models.BooleanField(verbose_name="Highly available")
    workload_type = models.ForeignKey(WorkloadType, verbose_name="Workload type")
    service_level = models.ForeignKey(ServiceLevel, verbose_name="Service level")
    eu_data_privacy_support = models.BooleanField(verbose_name="Eu data privacy support")
    disaster_recovery_enabled = models.BooleanField(verbose_name="Disaster recovery enabled")
    disaster_recovery_infrastructure_tenancy_preference = models.ForeignKey(DisasterRecoveryTenancy
                                                                            ,
                                                                            verbose_name="Disaster recovery infrastructure tenancy preference")
    lvm_level = models.ForeignKey(LvmLevel, verbose_name="Lvm level")
    hana_configuration = models.BooleanField(verbose_name="Hana configuration")
    database_type = models.ForeignKey(DatabaseType, verbose_name="Database type")
    sid_type = models.ForeignKey(SidType, verbose_name="Sid type")
    sap_offering = models.ForeignKey(SapOffering, verbose_name="Sap offering")
    migration_state = models.ForeignKey(MigrationState, verbose_name="Migration state")

    def __unicode__(self):
        return '->' + self.template.display_name + '->' + self.display_name

    class Meta:
        db_table = 'lama_template_target_sid'
        verbose_name = 'Lama template target sids'
        verbose_name_plural = 'Lama template target sidss'


class ServiceRoleDetail(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(ServiceRoleDetail, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    value = models.CharField(max_length=50, verbose_name='Value')
    servicerole = models.ForeignKey(ServiceRole, verbose_name='Servicerole')
    includes_eao_sap_application_support = models.BooleanField(verbose_name='Includes eao sap application support')
    tenant = models.ForeignKey(Tenant, verbose_name='Tenant')
    lifecycle_state = models.ForeignKey(LifecycleState, verbose_name='Lifecycle state')
    service_logo = models.CharField(max_length=100, verbose_name='Service logo')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'service_role_detail'
        verbose_name = 'Service role detail'
        verbose_name_plural = 'Service role details'


class LamaTemplateTargetSidService(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(LamaTemplateTargetSidService, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    sid = models.ForeignKey(LamaTemplateTargetSid, verbose_name='Sid')
    service_role = models.ForeignKey(ServiceRole, verbose_name='Service role')
    service_role_detail = models.ForeignKey(ServiceRoleDetail, verbose_name='Service role detail')
    topology = models.ForeignKey(Topology, verbose_name='Topology')
    instancehosts = models.ManyToManyField(LamaTemplateTargetSidInstanceHost, verbose_name='Instancehosts')

    def __unicode__(self):
        return self.sid.display_name + '->' + self.service_role.value

    class Meta:
        db_table = 'lama_template_target_sid_service'
        verbose_name = 'Lama template target sid service'
        verbose_name_plural = 'Lama template target sid Service'


class LamaTemplateTargetSidVolume(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(LamaTemplateTargetSidVolume, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    cpg = models.ForeignKey(Cpg, verbose_name='Cpg')
    datastore = models.ForeignKey(Datastore, verbose_name='Datastore')
    volume_type = models.ForeignKey(VolumeType, verbose_name='Volume type')
    display_name = models.CharField(max_length=40, verbose_name='Display name')
    size = models.IntegerField(verbose_name='Size')
    cg_name = models.CharField(max_length=40, verbose_name='Vg name')
    volumegrouptype = models.ForeignKey(VolumeGroupType, verbose_name='Volumegrouptype')
    instance_host = models.ForeignKey(LamaTemplateTargetSidInstanceHost, verbose_name='Instance host')
    migration_state = models.ForeignKey(MigrationState, verbose_name='Migration state')
    encryption_state = models.ForeignKey(EncryptionState, verbose_name='Encryption state')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'lama_template_target_sid_volume'
        verbose_name = 'Lama template target sid volume'
        verbose_name_plural = 'Lama template target sid Volume'


class Service(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Service, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    system = models.ForeignKey(System, verbose_name='System')
    service_role = models.ForeignKey(ServiceRole, verbose_name='Service role')
    service_role_detail = models.ForeignKey(ServiceRoleDetail, verbose_name='Service role detail')
    topology = models.ForeignKey(Topology, verbose_name='Topology')

    def __unicode__(self):
        pass

    class Meta:
        db_table = 'service'
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Service_vip(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Service_vip, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    service = models.ForeignKey(Service, verbose_name='Service')
    vlan = models.ForeignKey(Vlan, verbose_name='Vlan')
    ip_address = models.ForeignKey(IpAddressPool, verbose_name='Ip address')
    description = models.CharField(max_length=100, verbose_name='Description')

    def __unicode__(self):
        pass

    class Meta:
        db_table = 'service_vip'
        verbose_name = 'Service vip'
        verbose_name_plural = 'Service vips'


class SidLvmLicenseEvent(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(SidLvmLicenseEvent, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    sid = models.ForeignKey(System, verbose_name='Sid')
    lvm_level = models.ForeignKey(LvmLevel, verbose_name='Lvm level')
    event_type = models.ForeignKey(EventType, verbose_name='Event type')

    def __unicode__(self):
        pass

    class Meta:
        db_table = 'sid_lvm_license_event'
        verbose_name = 'Sid lvm license event'
        verbose_name_plural = 'Sid lvm license events'


class TenantUserGroup(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(TenantUserGroup, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    name = models.CharField(max_length=50, verbose_name='Name')
    tenant = models.ForeignKey(Tenant, verbose_name='Tenant')
    lifecycleactions = models.ManyToManyField(LifecycleAction, verbose_name='Lifecycleactions')
    system = models.ManyToManyField(System, verbose_name='System')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'tenant_user_group'
        verbose_name = 'Tenant user group'
        verbose_name_plural = 'Tenant user groups'


class VlanTriplet(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(VlanTriplet, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    production_vlan = models.ForeignKey(Vlan, related_name='VlanTriplet_production_vlan',
                                        verbose_name='Production vlan')
    internal_management_vlan = models.ForeignKey(Vlan, related_name='VlanTriplet_internal_management_vlan',
                                                 verbose_name='Internal management vlan')
    hsr_vlan = models.ForeignKey(Vlan, related_name='VlanTriplet_hsr_vlan', verbose_name='Hsr vlan')
    lifecycle_state = models.ForeignKey(LifecycleState, verbose_name='Lifecycle state')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'vlan_triplet'
        verbose_name = 'Vlan triplet'
        verbose_name_plural = 'Vlan triplets'


class Vla(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Vla, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    name = models.CharField(max_length=20, verbose_name='Name')
    lvm_host = models.ForeignKey(Lvm, verbose_name='Lvm host')
    url = models.URLField(verbose_name='Url')
    username = models.CharField(max_length=20, verbose_name='Username')
    password = models.CharField(max_length=20, verbose_name='Password')

    def __unicode__(self):
        return self.url

    class Meta:
        db_table = 'Vla'
        verbose_name = 'Vla'
        verbose_name_plural = 'Vlas'


class Vmnetwork(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Vmnetwork, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    name = models.CharField(max_length=50, verbose_name='Name')
    vlan = models.ForeignKey(Vlan, verbose_name='Vlan')

    def __unicode__(self):
        pass

    class Meta:
        db_table = 'vmnetwork'
        verbose_name = 'Vmnetwork'
        verbose_name_plural = 'Vmnetworks'


class VolumeGroup(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(VolumeGroup, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    display_name = models.CharField(max_length=100, verbose_name='Display name')
    type = models.ForeignKey(VolumeGroupType, verbose_name='Type')
    service = models.ForeignKey(Service, verbose_name='Service')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'volume_group'
        verbose_name = 'Volume group'
        verbose_name_plural = 'Volume groups'


class VolumeGroupFileSystem(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(VolumeGroupFileSystem, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    volume_group = models.ForeignKey(VolumeGroup, verbose_name='Volume group')
    mount_path = models.CharField(max_length=100, verbose_name='Mount path')
    size = models.CharField(max_length=100, verbose_name='Size')

    def __unicode__(self):
        pass

    class Meta:
        db_table = 'volume_group_file_System'
        verbose_name = 'Volume group file system'
        verbose_name_plural = 'Volume group file systems'


class Volume(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Volume, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    dpg = models.ForeignKey(Cpg, verbose_name='Cpg')
    datastore = models.ForeignKey(Datastore, verbose_name='Datastore')
    volume_group = models.ForeignKey(VolumeGroup, verbose_name='Volume group')
    volume_type = models.ForeignKey(VolumeType, verbose_name='Volume type')
    wwn = models.CharField(max_length=100, verbose_name='Wwn')
    display_name = models.CharField(max_length=100, verbose_name='Display name')
    size = models.IntegerField(verbose_name='Size')
    status = models.ForeignKey(StorageStatus, verbose_name='Status')
    instance_host = models.ForeignKey(InstanceHost, verbose_name='Instance host')
    migration_state = models.ForeignKey(MigrationState, verbose_name='Migration state')
    encryption_state = models.ForeignKey(EncryptionState, verbose_name='Encryption state')
    order_tracking = models.ForeignKey(OrderTracking, verbose_name='Order tracking')
    comment = models.CharField(max_length=100, verbose_name='Comment')

    def __unicode__(self):
        return self.display_name

    class Meta:
        db_table = 'volume'
        verbose_name = 'Volume'
        verbose_name_plural = 'Volumes'

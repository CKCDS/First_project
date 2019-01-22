# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from django.apps import AppConfig

from .models import *


class SodLvmConfig(AppConfig):
    name = 'SOD_LVM'


class ClusterAvailabilityLevelFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = ClusterAvailabilityLevel
        fields = '__all__'


class ClusterCpuOversubscriptionFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = ClusterCpuOversubscription
        fields = '__all__'


class ClusterMemoryOversubscriptionFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = ClusterMemoryOversubscription
        fields = '__all__'


class CpuArchitectureFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = CpuArchitecture
        fields = '__all__'


class CustomRamAngeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = CustomRamAnge
        fields = '__all__'


class DatabaseTypeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = DatabaseType
        fields = '__all__'


class DisasterRecoveryTenancyFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = DisasterRecoveryTenancy
        fields = '__all__'


class EncryptionStateFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = EncryptionState
        fields = '__all__'


class EsxHostCpuOversubscriptionFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = EsxHostCpuOversubscription
        fields = '__all__'


class EsxHostMemoryOversubscriptionFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = EsxHostMemoryOversubscription
        fields = '__all__'


class EventCategoryFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = EventCategory
        fields = '__all__'


class EventOriginFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = EventOrigin
        fields = '__all__'


class EventourceFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Eventource
        fields = '__all__'


class EventtatusFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Eventtatus
        fields = '__all__'


class EventTypeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = EventType
        fields = '__all__'


class HostStateFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = HostState
        fields = '__all__'


class Hp3parTierFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Hp3parTier
        fields = '__all__'


class IpAddressAllocationStateFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = IpAddressAllocationState
        fields = '__all__'


class IpAddressAllocationPurposeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = IpAddressAllocationPurpose
        fields = '__all__'


class LamaTemplateStateFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = LamaTemplateState
        fields = '__all__'


class LamaTemplateStatusFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = LamaTemplateStatus
        fields = '__all__'


class LicenseEventTypeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = LicenseEventType
        fields = '__all__'


class LifecycleActionTypeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = LifecycleActionType
        fields = '__all__'


class LifecycleStateFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = LifecycleState
        fields = '__all__'


class LvmLevelFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = LvmLevel
        fields = '__all__'


class LvmTypeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = LvmType
        fields = '__all__'


class MacAddressAllocationStateFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = MacAddressAllocationState
        fields = '__all__'


class MigrationStateFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = MigrationState
        fields = '__all__'


class SapOfferingFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = SapOffering
        fields = '__all__'


class ServiceLevelFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = ServiceLevel
        fields = '__all__'


class ServiceRoleFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = ServiceRole
        fields = '__all__'


class SidOriginFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = SidOrigin
        fields = '__all__'


class SidTypeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = SidType
        fields = '__all__'


class StorageStatusFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = StorageStatus
        fields = '__all__'


class StorageTypeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = StorageType
        fields = '__all__'


class StorageWorkloadTypeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = StorageWorkloadType
        fields = '__all__'


class SubscriptionStatusFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = SubscriptionStatus
        fields = '__all__'


class SuitabilityFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Suitability
        fields = '__all__'


class SupplierFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Supplier
        fields = '__all__'


class TicketClosureCodeInterpretationFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = TicketClosureCodeInterpretation
        fields = '__all__'


class TicketImplementationStatusFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = TicketImplementationStatus
        fields = '__all__'


class TicketOriginFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = TicketOrigin
        fields = '__all__'


class TickettateFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Tickettate
        fields = '__all__'


class TicketTypeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = TicketType
        fields = '__all__'


class TopologyFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Topology
        fields = '__all__'


class VirtualizationFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Virtualization
        fields = '__all__'


class VlanRoleFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = VlanRole
        fields = '__all__'


class VlanTypeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = VlanType
        fields = '__all__'


class VolumeGroupTypeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = VolumeGroupType
        fields = '__all__'


class VolumeTypeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = VolumeType
        fields = '__all__'


class WorkloadTypeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = WorkloadType
        fields = '__all__'


class ZoneFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Zone
        fields = '__all__'


class DataCenterFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = DataCenter
        fields = '__all__'


class VcenterFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Vcenter
        fields = '__all__'


class TenantFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Tenant
        fields = '__all__'


class ClusterFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Cluster
        fields = '__all__'


class Hp3parFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Hp3par
        fields = '__all__'


class CpgFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Cpg
        fields = '__all__'


class CustomCpuValueFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = CustomCpuValue
        fields = '__all__'


class TierFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Tier
        fields = '__all__'


class CustomSizeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = CustomSize
        fields = '__all__'


class DatastoreFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Datastore
        fields = '__all__'


class EsxHostFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = EsxHost
        fields = '__all__'


class EventCodeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = EventCode
        fields = '__all__'


class LvmFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Lvm
        fields = '__all__'


class OrderTrackingFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = OrderTracking
        fields = '__all__'


class SystemFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = System
        fields = '__all__'


class TicketClosureCodeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = TicketClosureCode
        fields = '__all__'


class TicketFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Ticket
        fields = '__all__'


class EventFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Event
        fields = '__all__'


class Hp3parCapacityFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Hp3parCapacity
        fields = '__all__'


class Hp3parPairFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Hp3parPair
        fields = '__all__'


class OperatingSystemFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = OperatingSystem
        fields = '__all__'


class ImageFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Image
        fields = '__all__'


class SizeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Size
        fields = '__all__'


class VlanFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Vlan
        fields = '__all__'


class InstanceHostFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = InstanceHost
        fields = '__all__'


class NicTypeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = NicType
        fields = '__all__'


class IpAddressPoolFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = IpAddressPool
        fields = '__all__'


class MacAddressPoolFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = MacAddressPool
        fields = '__all__'


class InstanceHostNicConfigFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = InstanceHostNicConfig
        fields = '__all__'


class LamaTemplateTargetSidInstanceHostFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = LamaTemplateTargetSidInstanceHost
        fields = '__all__'


class LamaTemplateTargetSidInstanceHostNicConfigFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = LamaTemplateTargetSidInstanceHostNicConfig
        fields = '__all__'


class LifecycleActionFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = LifecycleAction
        fields = '__all__'


class LamaTemplateFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = LamaTemplate
        fields = '__all__'


class LamaTemplateTargetSidFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = LamaTemplateTargetSid
        fields = '__all__'


class ServiceRoleDetailFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = ServiceRoleDetail
        fields = '__all__'


class LamaTemplateTargetSidServiceFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = LamaTemplateTargetSidService
        fields = '__all__'


class LamaTemplateTargetSidVolumeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = LamaTemplateTargetSidVolume
        fields = '__all__'


class ServiceFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Service
        fields = '__all__'


class Service_vipFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Service_vip
        fields = '__all__'


class SidLvmLicenseEventFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = SidLvmLicenseEvent
        fields = '__all__'


class TenantUserGroupFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = TenantUserGroup
        fields = '__all__'


class VlanTripletFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = VlanTriplet
        fields = '__all__'


class VlaFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Vla
        fields = '__all__'


class VmnetworkFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Vmnetwork
        fields = '__all__'


class VolumeGroupFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = VolumeGroup
        fields = '__all__'


class VolumeGroupFileSystemFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = VolumeGroupFileSystem
        fields = '__all__'


class VolumeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Volume
        fields = '__all__'

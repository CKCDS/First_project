# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from .serializers import *


# Create your views here.
class ClusterAvailabilityLevelList(generics.ListCreateAPIView):
    queryset = ClusterAvailabilityLevel.objects.all()
    serializer_class = ClusterAvailabilityLevelSerializer
    filter_fields = '__all__'


class ClusterAvailabilityLevelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClusterAvailabilityLevel.objects.all()
    serializer_class = ClusterAvailabilityLevelSerializer


class ClusterCpuOversubscriptionList(generics.ListCreateAPIView):
    queryset = ClusterCpuOversubscription.objects.all()
    serializer_class = ClusterCpuOversubscriptionSerializer
    filter_fields = '__all__'


class ClusterCpuOversubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClusterCpuOversubscription.objects.all()
    serializer_class = ClusterCpuOversubscriptionSerializer


class ClusterMemoryOversubscriptionList(generics.ListCreateAPIView):
    queryset = ClusterMemoryOversubscription.objects.all()
    serializer_class = ClusterMemoryOversubscriptionSerializer
    filter_fields = '__all__'


class ClusterMemoryOversubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClusterMemoryOversubscription.objects.all()
    serializer_class = ClusterMemoryOversubscriptionSerializer


class CpuArchitectureList(generics.ListCreateAPIView):
    queryset = CpuArchitecture.objects.all()
    serializer_class = CpuArchitectureSerializer
    filter_fields = '__all__'


class CpuArchitectureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CpuArchitecture.objects.all()
    serializer_class = CpuArchitectureSerializer


class CustomRamAngeList(generics.ListCreateAPIView):
    queryset = CustomRamAnge.objects.all()
    serializer_class = CustomRamAngeSerializer
    filter_fields = '__all__'


class CustomRamAngeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomRamAnge.objects.all()
    serializer_class = CustomRamAngeSerializer


class DatabaseTypeList(generics.ListCreateAPIView):
    queryset = DatabaseType.objects.all()
    serializer_class = DatabaseTypeSerializer
    filter_fields = '__all__'


class DatabaseTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatabaseType.objects.all()
    serializer_class = DatabaseTypeSerializer


class DisasterRecoveryTenancyList(generics.ListCreateAPIView):
    queryset = DisasterRecoveryTenancy.objects.all()
    serializer_class = DisasterRecoveryTenancySerializer
    filter_fields = '__all__'


class DisasterRecoveryTenancyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DisasterRecoveryTenancy.objects.all()
    serializer_class = DisasterRecoveryTenancySerializer


class EncryptionStateList(generics.ListCreateAPIView):
    queryset = EncryptionState.objects.all()
    serializer_class = EncryptionStateSerializer
    filter_fields = '__all__'


class EncryptionStateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EncryptionState.objects.all()
    serializer_class = EncryptionStateSerializer


class EsxHostCpuOversubscriptionList(generics.ListCreateAPIView):
    queryset = EsxHostCpuOversubscription.objects.all()
    serializer_class = EsxHostCpuOversubscriptionSerializer
    filter_fields = '__all__'


class EsxHostCpuOversubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EsxHostCpuOversubscription.objects.all()
    serializer_class = EsxHostCpuOversubscriptionSerializer


class EsxHostMemoryOversubscriptionList(generics.ListCreateAPIView):
    queryset = EsxHostMemoryOversubscription.objects.all()
    serializer_class = EsxHostMemoryOversubscriptionSerializer
    filter_fields = '__all__'


class EsxHostMemoryOversubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EsxHostMemoryOversubscription.objects.all()
    serializer_class = EsxHostMemoryOversubscriptionSerializer


class EventCategoryList(generics.ListCreateAPIView):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    filter_fields = '__all__'


class EventCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer


class EventOriginList(generics.ListCreateAPIView):
    queryset = EventOrigin.objects.all()
    serializer_class = EventOriginSerializer
    filter_fields = '__all__'


class EventOriginDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventOrigin.objects.all()
    serializer_class = EventOriginSerializer


class EventourceList(generics.ListCreateAPIView):
    queryset = Eventource.objects.all()
    serializer_class = EventourceSerializer
    filter_fields = '__all__'


class EventourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Eventource.objects.all()
    serializer_class = EventourceSerializer


class EventtatusList(generics.ListCreateAPIView):
    queryset = Eventtatus.objects.all()
    serializer_class = EventtatusSerializer
    filter_fields = '__all__'


class EventtatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Eventtatus.objects.all()
    serializer_class = EventtatusSerializer


class EventTypeList(generics.ListCreateAPIView):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
    filter_fields = '__all__'


class EventTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer


class HostStateList(generics.ListCreateAPIView):
    queryset = HostState.objects.all()
    serializer_class = HostStateSerializer
    filter_fields = '__all__'


class HostStateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HostState.objects.all()
    serializer_class = HostStateSerializer


class Hp3parTierList(generics.ListCreateAPIView):
    queryset = Hp3parTier.objects.all()
    serializer_class = Hp3parTierSerializer
    filter_fields = '__all__'


class Hp3parTierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hp3parTier.objects.all()
    serializer_class = Hp3parTierSerializer


class IpAddressAllocationStateList(generics.ListCreateAPIView):
    queryset = IpAddressAllocationState.objects.all()
    serializer_class = IpAddressAllocationStateSerializer
    filter_fields = '__all__'


class IpAddressAllocationStateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IpAddressAllocationState.objects.all()
    serializer_class = IpAddressAllocationStateSerializer


class IpAddressAllocationPurposeList(generics.ListCreateAPIView):
    queryset = IpAddressAllocationPurpose.objects.all()
    serializer_class = IpAddressAllocationPurposeSerializer
    filter_fields = '__all__'


class IpAddressAllocationPurposeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IpAddressAllocationPurpose.objects.all()
    serializer_class = IpAddressAllocationPurposeSerializer


class LamaTemplateStateList(generics.ListCreateAPIView):
    queryset = LamaTemplateState.objects.all()
    serializer_class = LamaTemplateStateSerializer
    filter_fields = '__all__'


class LamaTemplateStateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LamaTemplateState.objects.all()
    serializer_class = LamaTemplateStateSerializer


class LamaTemplateStatusList(generics.ListCreateAPIView):
    queryset = LamaTemplateStatus.objects.all()
    serializer_class = LamaTemplateStatusSerializer
    filter_fields = '__all__'


class LamaTemplateStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LamaTemplateStatus.objects.all()
    serializer_class = LamaTemplateStatusSerializer


class LicenseEventTypeList(generics.ListCreateAPIView):
    queryset = LicenseEventType.objects.all()
    serializer_class = LicenseEventTypeSerializer
    filter_fields = '__all__'


class LicenseEventTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LicenseEventType.objects.all()
    serializer_class = LicenseEventTypeSerializer


class LifecycleActionTypeList(generics.ListCreateAPIView):
    queryset = LifecycleActionType.objects.all()
    serializer_class = LifecycleActionTypeSerializer
    filter_fields = '__all__'


class LifecycleActionTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LifecycleActionType.objects.all()
    serializer_class = LifecycleActionTypeSerializer


class LifecycleStateList(generics.ListCreateAPIView):
    queryset = LifecycleState.objects.all()
    serializer_class = LifecycleStateSerializer
    filter_fields = '__all__'


class LifecycleStateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LifecycleState.objects.all()
    serializer_class = LifecycleStateSerializer


class LvmLevelList(generics.ListCreateAPIView):
    queryset = LvmLevel.objects.all()
    serializer_class = LvmLevelSerializer
    filter_fields = '__all__'


class LvmLevelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LvmLevel.objects.all()
    serializer_class = LvmLevelSerializer


class LvmTypeList(generics.ListCreateAPIView):
    queryset = LvmType.objects.all()
    serializer_class = LvmTypeSerializer
    filter_fields = '__all__'


class LvmTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LvmType.objects.all()
    serializer_class = LvmTypeSerializer


class MacAddressAllocationStateList(generics.ListCreateAPIView):
    queryset = MacAddressAllocationState.objects.all()
    serializer_class = MacAddressAllocationStateSerializer
    filter_fields = '__all__'


class MacAddressAllocationStateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MacAddressAllocationState.objects.all()
    serializer_class = MacAddressAllocationStateSerializer


class MigrationStateList(generics.ListCreateAPIView):
    queryset = MigrationState.objects.all()
    serializer_class = MigrationStateSerializer
    filter_fields = '__all__'


class MigrationStateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MigrationState.objects.all()
    serializer_class = MigrationStateSerializer


class SapOfferingList(generics.ListCreateAPIView):
    queryset = SapOffering.objects.all()
    serializer_class = SapOfferingSerializer
    filter_fields = '__all__'


class SapOfferingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SapOffering.objects.all()
    serializer_class = SapOfferingSerializer


class ServiceLevelList(generics.ListCreateAPIView):
    queryset = ServiceLevel.objects.all()
    serializer_class = ServiceLevelSerializer
    filter_fields = '__all__'


class ServiceLevelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceLevel.objects.all()
    serializer_class = ServiceLevelSerializer


class ServiceRoleList(generics.ListCreateAPIView):
    queryset = ServiceRole.objects.all()
    serializer_class = ServiceRoleSerializer
    filter_fields = '__all__'


class ServiceRoleDetail1(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceRole.objects.all()
    serializer_class = ServiceRoleSerializer


class SidOriginList(generics.ListCreateAPIView):
    queryset = SidOrigin.objects.all()
    serializer_class = SidOriginSerializer
    filter_fields = '__all__'


class SidOriginDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SidOrigin.objects.all()
    serializer_class = SidOriginSerializer


class SidTypeList(generics.ListCreateAPIView):
    queryset = SidType.objects.all()
    serializer_class = SidTypeSerializer
    filter_fields = '__all__'


class SidTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SidType.objects.all()
    serializer_class = SidTypeSerializer


class StorageStatusList(generics.ListCreateAPIView):
    queryset = StorageStatus.objects.all()
    serializer_class = StorageStatusSerializer
    filter_fields = '__all__'


class StorageStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StorageStatus.objects.all()
    serializer_class = StorageStatusSerializer


class StorageTypeList(generics.ListCreateAPIView):
    queryset = StorageType.objects.all()
    serializer_class = StorageTypeSerializer
    filter_fields = '__all__'


class StorageTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StorageType.objects.all()
    serializer_class = StorageTypeSerializer


class StorageWorkloadTypeList(generics.ListCreateAPIView):
    queryset = StorageWorkloadType.objects.all()
    serializer_class = StorageWorkloadTypeSerializer
    filter_fields = '__all__'


class StorageWorkloadTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StorageWorkloadType.objects.all()
    serializer_class = StorageWorkloadTypeSerializer


class SubscriptionStatusList(generics.ListCreateAPIView):
    queryset = SubscriptionStatus.objects.all()
    serializer_class = SubscriptionStatusSerializer
    filter_fields = '__all__'


class SubscriptionStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubscriptionStatus.objects.all()
    serializer_class = SubscriptionStatusSerializer


class SuitabilityList(generics.ListCreateAPIView):
    queryset = Suitability.objects.all()
    serializer_class = SuitabilitySerializer
    filter_fields = '__all__'


class SuitabilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Suitability.objects.all()
    serializer_class = SuitabilitySerializer


class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_fields = '__all__'


class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class TicketClosureCodeInterpretationList(generics.ListCreateAPIView):
    queryset = TicketClosureCodeInterpretation.objects.all()
    serializer_class = TicketClosureCodeInterpretationSerializer
    filter_fields = '__all__'


class TicketClosureCodeInterpretationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TicketClosureCodeInterpretation.objects.all()
    serializer_class = TicketClosureCodeInterpretationSerializer


class TicketImplementationStatusList(generics.ListCreateAPIView):
    queryset = TicketImplementationStatus.objects.all()
    serializer_class = TicketImplementationStatusSerializer
    filter_fields = '__all__'


class TicketImplementationStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TicketImplementationStatus.objects.all()
    serializer_class = TicketImplementationStatusSerializer


class TicketOriginList(generics.ListCreateAPIView):
    queryset = TicketOrigin.objects.all()
    serializer_class = TicketOriginSerializer
    filter_fields = '__all__'


class TicketOriginDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TicketOrigin.objects.all()
    serializer_class = TicketOriginSerializer


class TickettateList(generics.ListCreateAPIView):
    queryset = Tickettate.objects.all()
    serializer_class = TickettateSerializer
    filter_fields = '__all__'


class TickettateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tickettate.objects.all()
    serializer_class = TickettateSerializer


class TicketTypeList(generics.ListCreateAPIView):
    queryset = TicketType.objects.all()
    serializer_class = TicketTypeSerializer
    filter_fields = '__all__'


class TicketTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TicketType.objects.all()
    serializer_class = TicketTypeSerializer


class TopologyList(generics.ListCreateAPIView):
    queryset = Topology.objects.all()
    serializer_class = TopologySerializer
    filter_fields = '__all__'


class TopologyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topology.objects.all()
    serializer_class = TopologySerializer


class VirtualizationList(generics.ListCreateAPIView):
    queryset = Virtualization.objects.all()
    serializer_class = VirtualizationSerializer
    filter_fields = '__all__'


class VirtualizationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Virtualization.objects.all()
    serializer_class = VirtualizationSerializer


class VlanRoleList(generics.ListCreateAPIView):
    queryset = VlanRole.objects.all()
    serializer_class = VlanRoleSerializer
    filter_fields = '__all__'


class VlanRoleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VlanRole.objects.all()
    serializer_class = VlanRoleSerializer


class VlanTypeList(generics.ListCreateAPIView):
    queryset = VlanType.objects.all()
    serializer_class = VlanTypeSerializer
    filter_fields = '__all__'


class VlanTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VlanType.objects.all()
    serializer_class = VlanTypeSerializer


class VolumeGroupTypeList(generics.ListCreateAPIView):
    queryset = VolumeGroupType.objects.all()
    serializer_class = VolumeGroupTypeSerializer
    filter_fields = '__all__'


class VolumeGroupTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VolumeGroupType.objects.all()
    serializer_class = VolumeGroupTypeSerializer


class VolumeTypeList(generics.ListCreateAPIView):
    queryset = VolumeType.objects.all()
    serializer_class = VolumeTypeSerializer
    filter_fields = '__all__'


class VolumeTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VolumeType.objects.all()
    serializer_class = VolumeTypeSerializer


class WorkloadTypeList(generics.ListCreateAPIView):
    queryset = WorkloadType.objects.all()
    serializer_class = WorkloadTypeSerializer
    filter_fields = '__all__'


class WorkloadTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkloadType.objects.all()
    serializer_class = WorkloadTypeSerializer


class ZoneList(generics.ListCreateAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    filter_fields = '__all__'


class ZoneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer


class DataCenterList(generics.ListCreateAPIView):
    queryset = DataCenter.objects.all()
    serializer_class = DataCenterSerializer
    filter_fields = '__all__'


class DataCenterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataCenter.objects.all()
    serializer_class = DataCenterSerializer


class VcenterList(generics.ListCreateAPIView):
    queryset = Vcenter.objects.all()
    serializer_class = VcenterSerializer
    filter_fields = '__all__'


class VcenterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vcenter.objects.all()
    serializer_class = VcenterSerializer


class TenantList(generics.ListCreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    filter_fields = '__all__'


class TenantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class ClusterList(generics.ListCreateAPIView):
    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializer
    filter_fields = '__all__'


class ClusterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializer


class Hp3parList(generics.ListCreateAPIView):
    queryset = Hp3par.objects.all()
    serializer_class = Hp3parSerializer
    filter_fields = '__all__'


class Hp3parDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hp3par.objects.all()
    serializer_class = Hp3parSerializer


class CpgList(generics.ListCreateAPIView):
    queryset = Cpg.objects.all()
    serializer_class = CpgSerializer
    filter_fields = '__all__'


class CpgDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cpg.objects.all()
    serializer_class = CpgSerializer


class CustomCpuValueList(generics.ListCreateAPIView):
    queryset = CustomCpuValue.objects.all()
    serializer_class = CustomCpuValueSerializer
    filter_fields = '__all__'


class CustomCpuValueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomCpuValue.objects.all()
    serializer_class = CustomCpuValueSerializer


class TierList(generics.ListCreateAPIView):
    queryset = Tier.objects.all()
    serializer_class = TierSerializer
    filter_fields = '__all__'


class TierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tier.objects.all()
    serializer_class = TierSerializer


class CustomSizeList(generics.ListCreateAPIView):
    queryset = CustomSize.objects.all()
    serializer_class = CustomSizeSerializer
    filter_fields = '__all__'


class CustomSizeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomSize.objects.all()
    serializer_class = CustomSizeSerializer


class DatastoreList(generics.ListCreateAPIView):
    queryset = Datastore.objects.all()
    serializer_class = DatastoreSerializer
    filter_fields = '__all__'


class DatastoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Datastore.objects.all()
    serializer_class = DatastoreSerializer


class EsxHostList(generics.ListCreateAPIView):
    queryset = EsxHost.objects.all()
    serializer_class = EsxHostSerializer
    filter_fields = '__all__'


class EsxHostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EsxHost.objects.all()
    serializer_class = EsxHostSerializer


class EventCodeList(generics.ListCreateAPIView):
    queryset = EventCode.objects.all()
    serializer_class = EventCodeSerializer
    filter_fields = '__all__'


class EventCodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventCode.objects.all()
    serializer_class = EventCodeSerializer


class LvmList(generics.ListCreateAPIView):
    queryset = Lvm.objects.all()
    serializer_class = LvmSerializer
    filter_fields = '__all__'


class LvmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lvm.objects.all()
    serializer_class = LvmSerializer


class OrderTrackingList(generics.ListCreateAPIView):
    queryset = OrderTracking.objects.all()
    serializer_class = OrderTrackingSerializer
    filter_fields = '__all__'


class OrderTrackingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderTracking.objects.all()
    serializer_class = OrderTrackingSerializer


class SystemList(generics.ListCreateAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    filter_fields = '__all__'


class SystemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer


class TicketClosureCodeList(generics.ListCreateAPIView):
    queryset = TicketClosureCode.objects.all()
    serializer_class = TicketClosureCodeSerializer
    filter_fields = '__all__'


class TicketClosureCodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TicketClosureCode.objects.all()
    serializer_class = TicketClosureCodeSerializer


class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_fields = '__all__'


class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_fields = '__all__'


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class Hp3parCapacityList(generics.ListCreateAPIView):
    queryset = Hp3parCapacity.objects.all()
    serializer_class = Hp3parCapacitySerializer
    filter_fields = '__all__'


class Hp3parCapacityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hp3parCapacity.objects.all()
    serializer_class = Hp3parCapacitySerializer


class Hp3parPairList(generics.ListCreateAPIView):
    queryset = Hp3parPair.objects.all()
    serializer_class = Hp3parPairSerializer
    filter_fields = '__all__'


class Hp3parPairDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hp3parPair.objects.all()
    serializer_class = Hp3parPairSerializer


class OperatingSystemList(generics.ListCreateAPIView):
    queryset = OperatingSystem.objects.all()
    serializer_class = OperatingSystemSerializer
    filter_fields = '__all__'


class OperatingSystemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OperatingSystem.objects.all()
    serializer_class = OperatingSystemSerializer


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_fields = '__all__'


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class SizeList(generics.ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    filter_fields = '__all__'


class SizeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class VlanList(generics.ListCreateAPIView):
    queryset = Vlan.objects.all()
    serializer_class = VlanSerializer
    filter_fields = '__all__'


class VlanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vlan.objects.all()
    serializer_class = VlanSerializer


class InstanceHostList(generics.ListCreateAPIView):
    queryset = InstanceHost.objects.all()
    serializer_class = InstanceHostSerializer
    filter_fields = '__all__'


class InstanceHostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InstanceHost.objects.all()
    serializer_class = InstanceHostSerializer


class NicTypeList(generics.ListCreateAPIView):
    queryset = NicType.objects.all()
    serializer_class = NicTypeSerializer
    filter_fields = '__all__'


class NicTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NicType.objects.all()
    serializer_class = NicTypeSerializer


class IpAddressPoolList(generics.ListCreateAPIView):
    queryset = IpAddressPool.objects.all()
    serializer_class = IpAddressPoolSerializer
    filter_fields = '__all__'


class IpAddressPoolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IpAddressPool.objects.all()
    serializer_class = IpAddressPoolSerializer


class MacAddressPoolList(generics.ListCreateAPIView):
    queryset = MacAddressPool.objects.all()
    serializer_class = MacAddressPoolSerializer
    filter_fields = '__all__'


class MacAddressPoolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MacAddressPool.objects.all()
    serializer_class = MacAddressPoolSerializer


class InstanceHostNicConfigList(generics.ListCreateAPIView):
    queryset = InstanceHostNicConfig.objects.all()
    serializer_class = InstanceHostNicConfigSerializer
    filter_fields = '__all__'


class InstanceHostNicConfigDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InstanceHostNicConfig.objects.all()
    serializer_class = InstanceHostNicConfigSerializer


class LamaTemplateTargetSidInstanceHostList(generics.ListCreateAPIView):
    queryset = LamaTemplateTargetSidInstanceHost.objects.all()
    serializer_class = LamaTemplateTargetSidInstanceHostSerializer
    filter_fields = '__all__'


class LamaTemplateTargetSidInstanceHostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LamaTemplateTargetSidInstanceHost.objects.all()
    serializer_class = LamaTemplateTargetSidInstanceHostSerializer


class LamaTemplateTargetSidInstanceHostNicConfigList(generics.ListCreateAPIView):
    queryset = LamaTemplateTargetSidInstanceHostNicConfig.objects.all()
    serializer_class = LamaTemplateTargetSidInstanceHostNicConfigSerializer
    filter_fields = '__all__'


class LamaTemplateTargetSidInstanceHostNicConfigDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LamaTemplateTargetSidInstanceHostNicConfig.objects.all()
    serializer_class = LamaTemplateTargetSidInstanceHostNicConfigSerializer


class LifecycleActionList(generics.ListCreateAPIView):
    queryset = LifecycleAction.objects.all()
    serializer_class = LifecycleActionSerializer
    filter_fields = '__all__'


class LifecycleActionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LifecycleAction.objects.all()
    serializer_class = LifecycleActionSerializer


class LamaTemplateList(generics.ListCreateAPIView):
    queryset = LamaTemplate.objects.all()
    serializer_class = LamaTemplateSerializer
    filter_fields = '__all__'


class LamaTemplateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LamaTemplate.objects.all()
    serializer_class = LamaTemplateSerializer


class LamaTemplateTargetSidList(generics.ListCreateAPIView):
    queryset = LamaTemplateTargetSid.objects.all()
    serializer_class = LamaTemplateTargetSidSerializer
    filter_fields = '__all__'


class LamaTemplateTargetSidDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LamaTemplateTargetSid.objects.all()
    serializer_class = LamaTemplateTargetSidSerializer


class ServiceRoleDetailList(generics.ListCreateAPIView):
    queryset = ServiceRoleDetail.objects.all()
    serializer_class = ServiceRoleDetailSerializer
    filter_fields = '__all__'


class ServiceRoleDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceRoleDetail.objects.all()
    serializer_class = ServiceRoleDetailSerializer


class LamaTemplateTargetSidServiceList(generics.ListCreateAPIView):
    queryset = LamaTemplateTargetSidService.objects.all()
    serializer_class = LamaTemplateTargetSidServiceSerializer
    filter_fields = '__all__'


class LamaTemplateTargetSidServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LamaTemplateTargetSidService.objects.all()
    serializer_class = LamaTemplateTargetSidServiceSerializer


class LamaTemplateTargetSidVolumeList(generics.ListCreateAPIView):
    queryset = LamaTemplateTargetSidVolume.objects.all()
    serializer_class = LamaTemplateTargetSidVolumeSerializer
    filter_fields = '__all__'


class LamaTemplateTargetSidVolumeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LamaTemplateTargetSidVolume.objects.all()
    serializer_class = LamaTemplateTargetSidVolumeSerializer


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_fields = '__all__'


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class Service_vipList(generics.ListCreateAPIView):
    queryset = Service_vip.objects.all()
    serializer_class = Service_vipSerializer
    filter_fields = '__all__'


class Service_vipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service_vip.objects.all()
    serializer_class = Service_vipSerializer


class SidLvmLicenseEventList(generics.ListCreateAPIView):
    queryset = SidLvmLicenseEvent.objects.all()
    serializer_class = SidLvmLicenseEventSerializer
    filter_fields = '__all__'


class SidLvmLicenseEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SidLvmLicenseEvent.objects.all()
    serializer_class = SidLvmLicenseEventSerializer


class TenantUserGroupList(generics.ListCreateAPIView):
    queryset = TenantUserGroup.objects.all()
    serializer_class = TenantUserGroupSerializer
    filter_fields = '__all__'


class TenantUserGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TenantUserGroup.objects.all()
    serializer_class = TenantUserGroupSerializer


class VlanTripletList(generics.ListCreateAPIView):
    queryset = VlanTriplet.objects.all()
    serializer_class = VlanTripletSerializer
    filter_fields = '__all__'


class VlanTripletDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VlanTriplet.objects.all()
    serializer_class = VlanTripletSerializer


class VlaList(generics.ListCreateAPIView):
    queryset = Vla.objects.all()
    serializer_class = VlaSerializer
    filter_fields = '__all__'


class VlaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vla.objects.all()
    serializer_class = VlaSerializer


class VmnetworkList(generics.ListCreateAPIView):
    queryset = Vmnetwork.objects.all()
    serializer_class = VmnetworkSerializer
    filter_fields = '__all__'


class VmnetworkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vmnetwork.objects.all()
    serializer_class = VmnetworkSerializer


class VolumeGroupList(generics.ListCreateAPIView):
    queryset = VolumeGroup.objects.all()
    serializer_class = VolumeGroupSerializer
    filter_fields = '__all__'


class VolumeGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VolumeGroup.objects.all()
    serializer_class = VolumeGroupSerializer


class VolumeGroupFileSystemList(generics.ListCreateAPIView):
    queryset = VolumeGroupFileSystem.objects.all()
    serializer_class = VolumeGroupFileSystemSerializer
    filter_fields = '__all__'


class VolumeGroupFileSystemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VolumeGroupFileSystem.objects.all()
    serializer_class = VolumeGroupFileSystemSerializer


class VolumeList(generics.ListCreateAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    filter_fields = '__all__'


class VolumeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer

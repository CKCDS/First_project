from rest_framework import serializers

from .models import *


class ClusterAvailabilityLevelSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()


    class Meta:
        model = ClusterAvailabilityLevel
        fields = '__all__'

class ClusterCpuOversubscriptionSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()


    class Meta:
        model = ClusterCpuOversubscription
        fields = '__all__'


class ClusterMemoryOversubscriptionSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = ClusterMemoryOversubscription
        fields = '__all__'


class CpuArchitectureSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = CpuArchitecture
        fields = '__all__'


class CustomRamAngeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = CustomRamAnge
        fields = '__all__'


class DatabaseTypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = DatabaseType
        fields = '__all__'


class DisasterRecoveryTenancySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = DisasterRecoveryTenancy
        fields = '__all__'


class EncryptionStateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = EncryptionState
        fields = '__all__'


class EsxHostCpuOversubscriptionSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = EsxHostCpuOversubscription
        fields = '__all__'


class EsxHostMemoryOversubscriptionSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = EsxHostMemoryOversubscription
        fields = '__all__'


class EventCategorySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = EventCategory
        fields = '__all__'


class EventOriginSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = EventOrigin
        fields = '__all__'


class EventourceSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Eventource
        fields = '__all__'


class EventtatusSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Eventtatus
        fields = '__all__'


class EventTypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = EventType
        fields = '__all__'


class HostStateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = HostState
        fields = '__all__'


class Hp3parTierSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Hp3parTier
        fields = '__all__'


class IpAddressAllocationStateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = IpAddressAllocationState
        fields = '__all__'


class IpAddressAllocationPurposeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = IpAddressAllocationPurpose
        fields = '__all__'


class LamaTemplateStateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = LamaTemplateState
        fields = '__all__'


class LamaTemplateStatusSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = LamaTemplateStatus
        fields = '__all__'


class LicenseEventTypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = LicenseEventType
        fields = '__all__'


class LifecycleActionTypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = LifecycleActionType
        fields = '__all__'


class LifecycleStateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = LifecycleState
        fields = '__all__'


class LvmLevelSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = LvmLevel
        fields = '__all__'


class LvmTypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = LvmType
        fields = '__all__'


class MacAddressAllocationStateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = MacAddressAllocationState
        fields = '__all__'


class MigrationStateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = MigrationState
        fields = '__all__'


class SapOfferingSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = SapOffering
        fields = '__all__'


class ServiceLevelSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = ServiceLevel
        fields = '__all__'


class ServiceRoleSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = ServiceRole
        fields = '__all__'


class SidOriginSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = SidOrigin
        fields = '__all__'


class SidTypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = SidType
        fields = '__all__'


class StorageStatusSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = StorageStatus
        fields = '__all__'


class StorageTypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = StorageType
        fields = '__all__'


class StorageWorkloadTypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = StorageWorkloadType
        fields = '__all__'


class SubscriptionStatusSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = SubscriptionStatus
        fields = '__all__'


class SuitabilitySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Suitability
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Supplier
        fields = '__all__'


class TicketClosureCodeInterpretationSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = TicketClosureCodeInterpretation
        fields = '__all__'


class TicketImplementationStatusSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = TicketImplementationStatus
        fields = '__all__'


class TicketOriginSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = TicketOrigin
        fields = '__all__'


class TickettateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Tickettate
        fields = '__all__'


class TicketTypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = TicketType
        fields = '__all__'


class TopologySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Topology
        fields = '__all__'


class VirtualizationSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Virtualization
        fields = '__all__'


class VlanRoleSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = VlanRole
        fields = '__all__'


class VlanTypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = VlanType
        fields = '__all__'


class VolumeGroupTypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = VolumeGroupType
        fields = '__all__'


class VolumeTypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = VolumeType
        fields = '__all__'


class WorkloadTypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = WorkloadType
        fields = '__all__'


class ZoneSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Zone
        fields = '__all__'


class DataCenterSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = DataCenter
        fields = '__all__'


class VcenterSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Vcenter
        fields = '__all__'


class TenantSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Tenant
        fields = '__all__'


class ClusterSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Cluster
        fields = '__all__'


class Hp3parSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Hp3par
        fields = '__all__'


class CpgSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Cpg
        fields = '__all__'


class CustomCpuValueSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = CustomCpuValue
        fields = '__all__'


class TierSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Tier
        fields = '__all__'


class CustomSizeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = CustomSize
        fields = '__all__'


class DatastoreSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Datastore
        fields = '__all__'


class EsxHostSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = EsxHost
        fields = '__all__'


class EventCodeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = EventCode
        fields = '__all__'


class LvmSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Lvm
        fields = '__all__'


class OrderTrackingSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = OrderTracking
        fields = '__all__'


class SystemSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = System
        fields = '__all__'


class TicketClosureCodeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = TicketClosureCode
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Ticket
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Event
        fields = '__all__'


class Hp3parCapacitySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Hp3parCapacity
        fields = '__all__'


class Hp3parPairSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Hp3parPair
        fields = '__all__'


class OperatingSystemSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = OperatingSystem
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Image
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Size
        fields = '__all__'


class VlanSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Vlan
        fields = '__all__'


class InstanceHostSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = InstanceHost
        fields = '__all__'


class NicTypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = NicType
        fields = '__all__'


class IpAddressPoolSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = IpAddressPool
        fields = '__all__'


class MacAddressPoolSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = MacAddressPool
        fields = '__all__'


class InstanceHostNicConfigSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = InstanceHostNicConfig
        fields = '__all__'


class LamaTemplateTargetSidInstanceHostSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = LamaTemplateTargetSidInstanceHost
        fields = '__all__'


class LamaTemplateTargetSidInstanceHostNicConfigSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = LamaTemplateTargetSidInstanceHostNicConfig
        fields = '__all__'


class LifecycleActionSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = LifecycleAction
        fields = '__all__'


class LamaTemplateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = LamaTemplate
        fields = '__all__'


class LamaTemplateTargetSidSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = LamaTemplateTargetSid
        fields = '__all__'


class ServiceRoleDetailSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = ServiceRoleDetail
        fields = '__all__'


class LamaTemplateTargetSidServiceSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = LamaTemplateTargetSidService
        fields = '__all__'


class LamaTemplateTargetSidVolumeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = LamaTemplateTargetSidVolume
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Service
        fields = '__all__'


class Service_vipSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Service_vip
        fields = '__all__'


class SidLvmLicenseEventSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = SidLvmLicenseEvent
        fields = '__all__'


class TenantUserGroupSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = TenantUserGroup
        fields = '__all__'


class VlanTripletSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = VlanTriplet
        fields = '__all__'


class VlaSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Vla
        fields = '__all__'


class VmnetworkSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Vmnetwork
        fields = '__all__'


class VolumeGroupSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = VolumeGroup
        fields = '__all__'


class VolumeGroupFileSystemSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = VolumeGroupFileSystem
        fields = '__all__'


class VolumeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Volume
        fields = '__all__'

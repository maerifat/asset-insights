import boto3
from lxml import etree
prod_session= boto3.Session(profile_name='prod')

regions= ['ap-south-1', 'us-east-1']


services=('AWS::EC2::CustomerGateway',
'AWS::EC2::EIP',
'AWS::EC2::Host',
'AWS::EC2::Instance',
'AWS::EC2::InternetGateway',
'AWS::EC2::NetworkAcl',
'AWS::EC2::NetworkInterface',
'AWS::EC2::RouteTable',
'AWS::EC2::SecurityGroup',
'AWS::EC2::Subnet',
'AWS::CloudTrail::Trail',
'AWS::EC2::Volume',
'AWS::EC2::VPC',
'AWS::EC2::VPNConnection',
'AWS::EC2::VPNGateway',
'AWS::EC2::RegisteredHAInstance',
'AWS::EC2::NatGateway',
'AWS::EC2::EgressOnlyInternetGateway',
'AWS::EC2::VPCEndpoint',
'AWS::EC2::VPCEndpointService',
'AWS::EC2::FlowLog',
'AWS::EC2::VPCPeeringConnection',
'AWS::Elasticsearch::Domain',
'AWS::IAM::Group',
'AWS::IAM::Policy',
'AWS::IAM::Role',
'AWS::IAM::User',
'AWS::ElasticLoadBalancingV2::LoadBalancer',
'AWS::ACM::Certificate',
'AWS::RDS::DBInstance',
'AWS::RDS::DBSubnetGroup',
'AWS::RDS::DBSecurityGroup',
'AWS::RDS::DBSnapshot',
'AWS::RDS::DBCluster',
'AWS::RDS::DBClusterSnapshot',
'AWS::RDS::EventSubscription',
'AWS::S3::Bucket',
'AWS::S3::AccountPublicAccessBlock',
'AWS::Redshift::Cluster',
'AWS::Redshift::ClusterSnapshot',
'AWS::Redshift::ClusterParameterGroup',
'AWS::Redshift::ClusterSecurityGroup',
'AWS::Redshift::ClusterSubnetGroup',
'AWS::Redshift::EventSubscription',
'AWS::SSM::ManagedInstanceInventory',
'AWS::CloudWatch::Alarm',
'AWS::CloudFormation::Stack',
'AWS::ElasticLoadBalancing::LoadBalancer',
'AWS::AutoScaling::AutoScalingGroup',
'AWS::AutoScaling::LaunchConfiguration',
'AWS::AutoScaling::ScalingPolicy',
'AWS::AutoScaling::ScheduledAction',
'AWS::DynamoDB::Table',
'AWS::CodeBuild::Project',
'AWS::WAF::RateBasedRule',
'AWS::WAF::Rule',
'AWS::WAF::RuleGroup',
'AWS::WAF::WebACL',
'AWS::WAFRegional::RateBasedRule',
'AWS::WAFRegional::Rule',
'AWS::WAFRegional::RuleGroup',
'AWS::WAFRegional::WebACL',
'AWS::CloudFront::Distribution',
'AWS::CloudFront::StreamingDistribution',
'AWS::Lambda::Function',
'AWS::NetworkFirewall::Firewall',
'AWS::NetworkFirewall::FirewallPolicy',
'AWS::NetworkFirewall::RuleGroup',
'AWS::ElasticBeanstalk::Application',
'AWS::ElasticBeanstalk::ApplicationVersion',
'AWS::ElasticBeanstalk::Environment',
'AWS::WAFv2::WebACL',
'AWS::WAFv2::RuleGroup',
'AWS::WAFv2::IPSet',
'AWS::WAFv2::RegexPatternSet',
'AWS::WAFv2::ManagedRuleSet',
'AWS::XRay::EncryptionConfig',
'AWS::SSM::AssociationCompliance',
'AWS::SSM::PatchCompliance',
'AWS::Shield::Protection',
'AWS::ShieldRegional::Protection',
'AWS::ApiGateway::Stage',
'AWS::ApiGateway::RestApi',
'AWS::ApiGatewayV2::Stage',
'AWS::ApiGatewayV2::Api',
'AWS::CodePipeline::Pipeline',
'AWS::ServiceCatalog::CloudFormationProvisionedProduct',
'AWS::ServiceCatalog::CloudFormationProduct',
'AWS::ServiceCatalog::Portfolio',
'AWS::SQS::Queue',
'AWS::KMS::Key',
'AWS::QLDB::Ledger',
'AWS::SecretsManager::Secret',
'AWS::SNS::Topic',
'AWS::SSM::FileData',
'AWS::Backup::BackupPlan',
'AWS::Backup::BackupSelection',
'AWS::Backup::BackupVault',
'AWS::Backup::RecoveryPoint',
'AWS::ECR::Repository',
'AWS::ECS::Cluster',
'AWS::ECS::Service',
'AWS::ECS::TaskDefinition',
'AWS::EFS::AccessPoint',
'AWS::EFS::FileSystem',
'AWS::EKS::Cluster',
'AWS::OpenSearch::Domain',
'AWS::EC2::TransitGateway',
'AWS::Kinesis::Stream',
'AWS::Kinesis::StreamConsumer',
'AWS::CodeDeploy::Application',
'AWS::CodeDeploy::DeploymentConfig',
'AWS::CodeDeploy::DeploymentGroup',
'AWS::EC2::LaunchTemplate',
'AWS::ECR::PublicRepository',
'AWS::GuardDuty::Detector',
'AWS::EMR::SecurityConfiguration',
'AWS::SageMaker::CodeRepository',
'AWS::Route53Resolver::ResolverEndpoint',
'AWS::Route53Resolver::ResolverRule',
'AWS::Route53Resolver::ResolverRuleAssociation',
'AWS::DMS::ReplicationSubnetGroup',
'AWS::DMS::EventSubscription',
'AWS::MSK::Cluster',
'AWS::StepFunctions::Activity',
'AWS::WorkSpaces::Workspace',
'AWS::WorkSpaces::ConnectionAlias',
'AWS::SageMaker::Model',
'AWS::ElasticLoadBalancingV2::Listener',
'AWS::StepFunctions::StateMachine',
'AWS::Batch::JobQueue',
'AWS::Batch::ComputeEnvironment',
'AWS::AccessAnalyzer::Analyzer',
'AWS::Athena::WorkGroup',
'AWS::Athena::DataCatalog',
'AWS::Detective::Graph',
'AWS::GlobalAccelerator::Accelerator',
'AWS::GlobalAccelerator::EndpointGroup',
'AWS::GlobalAccelerator::Listener',
'AWS::EC2::TransitGatewayAttachment',
'AWS::EC2::TransitGatewayRouteTable',
'AWS::DMS::Certificate',
'AWS::AppConfig::Application',
'AWS::AppSync::GraphQLApi',
'AWS::DataSync::LocationSMB',
'AWS::DataSync::LocationFSxLustre',
'AWS::DataSync::LocationS3',
'AWS::DataSync::LocationEFS',
'AWS::DataSync::Task',
'AWS::DataSync::LocationNFS',
'AWS::EC2::NetworkInsightsAccessScopeAnalysis',
'AWS::EKS::FargateProfile',
'AWS::Glue::Job',
'AWS::GuardDuty::ThreatIntelSet',
'AWS::GuardDuty::IPSet',
'AWS::SageMaker::Workteam',
'AWS::SageMaker::NotebookInstanceLifecycleConfig',
'AWS::ServiceDiscovery::Service',
'AWS::ServiceDiscovery::PublicDnsNamespace',
'AWS::SES::ContactList',
'AWS::SES::ConfigurationSet',
'AWS::Route53::HostedZone',
'AWS::IoTEvents::Input',
'AWS::IoTEvents::DetectorModel',
'AWS::IoTEvents::AlarmModel',
'AWS::ServiceDiscovery::HttpNamespace',
'AWS::Events::EventBus',
'AWS::ImageBuilder::ContainerRecipe',
'AWS::ImageBuilder::DistributionConfiguration',
'AWS::ImageBuilder::InfrastructureConfiguration',
'AWS::DataSync::LocationObjectStorage',
'AWS::DataSync::LocationHDFS',
'AWS::Glue::Classifier',
'AWS::Route53RecoveryReadiness::Cell',
'AWS::Route53RecoveryReadiness::ReadinessCheck',
'AWS::ECR::RegistryPolicy',
'AWS::Backup::ReportPlan',
'AWS::Lightsail::Certificate',
'AWS::RUM::AppMonitor',
'AWS::Events::Endpoint',
'AWS::SES::ReceiptRuleSet',
'AWS::Events::Archive',
'AWS::Events::ApiDestination',
'AWS::Lightsail::Disk',
'AWS::FIS::ExperimentTemplate',
'AWS::DataSync::LocationFSxWindows',
'AWS::SES::ReceiptFilter',
'AWS::GuardDuty::Filter',
'AWS::SES::Template',
'AWS::AmazonMQ::Broker',
'AWS::AppConfig::Environment',
'AWS::AppConfig::ConfigurationProfile',
'AWS::Cloud9::EnvironmentEC2',
'AWS::EventSchemas::Registry',
'AWS::EventSchemas::RegistryPolicy',
'AWS::EventSchemas::Discoverer',
'AWS::FraudDetector::Label',
'AWS::FraudDetector::EntityType',
'AWS::FraudDetector::Variable',
'AWS::FraudDetector::Outcome',
'AWS::IoT::Authorizer',
'AWS::IoT::SecurityProfile',
'AWS::IoT::RoleAlias',
'AWS::IoT::Dimension',
'AWS::IoTAnalytics::Datastore',
'AWS::Lightsail::Bucket',
'AWS::Lightsail::StaticIp',
'AWS::MediaPackage::PackagingGroup',
'AWS::Route53RecoveryReadiness::RecoveryGroup',
'AWS::ResilienceHub::ResiliencyPolicy',
'AWS::Transfer::Workflow',
'AWS::EKS::IdentityProviderConfig',
'AWS::EKS::Addon',
'AWS::Glue::MLTransform',
'AWS::IoT::Policy',
'AWS::IoT::MitigationAction',
'AWS::IoTTwinMaker::Workspace',
'AWS::IoTTwinMaker::Entity',
'AWS::IoTAnalytics::Dataset',
'AWS::IoTAnalytics::Pipeline',
'AWS::IoTAnalytics::Channel',
'AWS::IoTSiteWise::Dashboard',
'AWS::IoTSiteWise::Project',
'AWS::IoTSiteWise::Portal',
'AWS::IoTSiteWise::AssetModel',
'AWS::IVS::Channel',
'AWS::IVS::RecordingConfiguration',
'AWS::IVS::PlaybackKeyPair',
'AWS::KinesisAnalyticsV2::Application',
'AWS::RDS::GlobalCluster',
'AWS::S3::MultiRegionAccessPoint',
'AWS::DeviceFarm::TestGridProject',
'AWS::Budgets::BudgetsAction',
'AWS::Lex::Bot',
'AWS::CodeGuruReviewer::RepositoryAssociation',
'AWS::IoT::CustomMetric',
'AWS::Route53Resolver::FirewallDomainList',
'AWS::RoboMaker::RobotApplicationVersion',
'AWS::EC2::TrafficMirrorSession',
'AWS::IoTSiteWise::Gateway',
'AWS::Lex::BotAlias',
'AWS::LookoutMetrics::Alert',
'AWS::IoT::AccountAuditConfiguration',
'AWS::EC2::TrafficMirrorTarget',
'AWS::S3::StorageLens',
'AWS::IoT::ScheduledAudit',
'AWS::Events::Connection',
'AWS::EventSchemas::Schema',
'AWS::MediaPackage::PackagingConfiguration',
'AWS::KinesisVideo::SignalingChannel',
'AWS::AppStream::DirectoryConfig',
'AWS::LookoutVision::Project',
'AWS::Route53RecoveryControl::Cluster',
'AWS::Route53RecoveryControl::SafetyRule',
'AWS::Route53RecoveryControl::ControlPanel',
'AWS::Route53RecoveryControl::RoutingControl',
'AWS::Route53RecoveryReadiness::ResourceSet',
'AWS::RoboMaker::SimulationApplication',
'AWS::RoboMaker::RobotApplication',
'AWS::HealthLake::FHIRDatastore',
'AWS::Pinpoint::Segment',
'AWS::Pinpoint::ApplicationSettings',
'AWS::Events::Rule',
'AWS::EC2::DHCPOptions',
'AWS::EC2::NetworkInsightsPath',
'AWS::EC2::TrafficMirrorFilter',
'AWS::EC2::IPAM',
'AWS::IoTTwinMaker::Scene',
'AWS::NetworkManager::TransitGatewayRegistration',
'AWS::CustomerProfiles::Domain',
'AWS::AutoScaling::WarmPool',
'AWS::Connect::PhoneNumber',
'AWS::AppConfig::DeploymentStrategy',
'AWS::AppFlow::Flow',
'AWS::AuditManager::Assessment',
'AWS::CloudWatch::MetricStream',
'AWS::DeviceFarm::InstanceProfile',
'AWS::DeviceFarm::Project',
'AWS::EC2::EC2Fleet',
'AWS::EC2::SubnetRouteTableAssociation',
'AWS::ECR::PullThroughCacheRule',
'AWS::GroundStation::Config',
'AWS::ImageBuilder::ImagePipeline',
'AWS::IoT::FleetMetric',
'AWS::IoTWireless::ServiceProfile',
'AWS::NetworkManager::Device',
'AWS::NetworkManager::GlobalNetwork',
'AWS::NetworkManager::Link',
'AWS::NetworkManager::Site',
'AWS::Panorama::Package',
'AWS::Pinpoint::App',
'AWS::Redshift::ScheduledAction',
'AWS::Route53Resolver::FirewallRuleGroupAssociation',
'AWS::SageMaker::AppImageConfig',
'AWS::SageMaker::Image',
'AWS::Config::ConformancePackCompliance',
'AWS::Config::ResourceCompliance')



def find_resource(service):
    service_resources=[]
    config_client= prod_session.client('config',region_name='ap-south-1')
    response = config_client.list_discovered_resources(
        resourceType=service,
        includeDeletedResources=False
    )





    try:
       
        y=0
        service_resources=[]
        accounttree= etree.SubElement(root,'ul',attrib={'style': 'color: #333333;font-weight: bold;font-size: 15px'},nsmap=None)
        servicename= f"s{x}"
        servicename=etree.SubElement(accounttree,'li',attrib={'style': 'color: #009900;font-weight: bold;font-size: 15px'},nsmap=None)
        servicename.text=service
        for region in regions:


            
            config_client= prod_session.client('config',region_name=region)
            response = config_client.list_discovered_resources(
                resourceType=service,
                includeDeletedResources=False
            )


            for resource in response['resourceIdentifiers']:
                resourceused= f"{resource['resourceId']} [{region}]"
                #({resource['resourceName']})"
                service_resources.append(resourceused)
        for service_resource in service_resources:
            y=y+1
            resourcetree=etree.SubElement(servicename,'ul',attrib=None,nsmap=None)
            resourcename=f"s{x}r{y}"
            if "ap-south-1" in service_resource:
                resourcename=etree.SubElement(resourcetree,'li',attrib={'style': 'color: #0066CC ;font-weight: normal;font-size: 15px'},nsmap=None)
            else:
                resourcename=etree.SubElement(resourcetree,'li',attrib={'style': 'color: red ;font-weight: normal;font-size: 15px'},nsmap=None)
            resourcename.text=f"{service_resource}"
        


        print(service)
        print(service_resources)


    except Exception as e:

        print(f"An error occured {e}in {service}")
        print(response)
        print()
        print()






# Create child elements



root = etree.Element('ul',attrib={'style': 'color: maroon;font-weight: bold;font-size: 22px'},nsmap=None)
root.text=f"Prod Account"

x=0
for service in services:
    x=x+1
    find_resource(service)

pagestyle ="""<!DOCTYPE html>
<html>
  <head>
    <title>Rainbow Border</title>
    <style>
      body {
        padding: 5px;
  
        border: 3px solid;
        border-image-slice: 1;
        border-image-source: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
        border-image-repeat: round;
        padding: 5px;
      }

      @keyframes changeColor {
        0% {
            color: lightgree;
        }
        16.7% {
            color: blue;
        }
        33.3% {
            color: rgb(91, 36, 180);
        }
        50% {
            color: orange;
        }
        66.7% {
            color: purple;
        }
        83.3% {
            color: pink;
        }
        100% {
            color: blue;
        }
    }

      h2 {
            animation: changeColor 15s ease-in-out infinite;text-align: center;
    }
    </style>
  </head>
  <body>
    <div class="content">
      <h2>AWS Asset Inventory</h2>

    </div>
  </body>
</html>

""" 


from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

html_string = pagestyle.encode() + etree.tostring(root)
html_string+= f'''<footer><p>Generated by Rupifi Security Team on {dt_string} as part of the ClearSky Security Project.</p></footer>'''.encode()

# Save the HTML to a file
with open('assetinventory.html', 'w') as file:
    file.write(html_string.decode("utf-8"))





print("assetinventory.html saved successfully.")
#find_resource('AWS::EC2::SecurityGroup')



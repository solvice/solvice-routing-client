# SolviceRoutingClient - the C# library for the Solvice API

No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This C# SDK is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0-oas3
- SDK version: 0.9
- Build package: io.swagger.codegen.v3.generators.dotnet.CSharpClientCodegen

<a name="frameworks-supported"></a>
## Frameworks supported
- .NET 4.0 or later
- Windows Phone 7.1 (Mango)

<a name="dependencies"></a>
## Dependencies
- [RestSharp](https://www.nuget.org/packages/RestSharp) - 105.1.0 or later
- [Json.NET](https://www.nuget.org/packages/Newtonsoft.Json/) - 7.0.0 or later
- [JsonSubTypes](https://www.nuget.org/packages/JsonSubTypes/) - 1.2.0 or later

The DLLs included in the package may not be the latest version. We recommend using [NuGet](https://docs.nuget.org/consume/installing-nuget) to obtain the latest version of the packages:
```
Install-Package RestSharp
Install-Package Newtonsoft.Json
Install-Package JsonSubTypes
```

NOTE: RestSharp versions greater than 105.1.0 have a bug which causes file uploads to fail. See [RestSharp#742](https://github.com/restsharp/RestSharp/issues/742)

<a name="installation"></a>
## Installation
Run the following command to generate the DLL
- [Mac/Linux] `/bin/sh build.sh`
- [Windows] `build.bat`

Then include the DLL (under the `bin` folder) in the C# project, and use the namespaces:
```csharp
using SolviceRoutingClient.Api;
using SolviceRoutingClient.Client;
using SolviceRoutingClient.Model;
```
<a name="packaging"></a>
## Packaging

A `.nuspec` is included with the project. You can follow the Nuget quickstart to [create](https://docs.microsoft.com/en-us/nuget/quickstart/create-and-publish-a-package#create-the-package) and [publish](https://docs.microsoft.com/en-us/nuget/quickstart/create-and-publish-a-package#publish-the-package) packages.

This `.nuspec` uses placeholders from the `.csproj`, so build the `.csproj` directly:

```
nuget pack -Build -OutputDirectory out SolviceRoutingClient.csproj
```

Then, publish to a [local feed](https://docs.microsoft.com/en-us/nuget/hosting-packages/local-feeds) or [other host](https://docs.microsoft.com/en-us/nuget/hosting-packages/overview) and consume the new package via Nuget as usual.

<a name="getting-started"></a>
## Getting Started

```csharp
using System;
using System.Diagnostics;
using SolviceRoutingClient.Api;
using SolviceRoutingClient.Client;
using SolviceRoutingClient.Model;

namespace Example
{
    public class Example
    {
        public void main()
        {
            // Configure HTTP basic authorization: basicAuth
            Configuration.Default.Username = "YOUR_USERNAME";
            Configuration.Default.Password = "YOUR_PASSWORD";

            var apiInstance = new PDPApi();
            var jobId = jobId_example;  // string | The job ID.

            try
            {
                // gets a job
                Job result = apiInstance.GetJob(jobId);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling PDPApi.GetJob: " + e.Message );
            }
        }
    }
}
```

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://api.solvice.io/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PDPApi* | [**GetJob**](docs/PDPApi.md#getjob) | **GET** /jobs/{jobId} | gets a job
*PDPApi* | [**GetJobStatus**](docs/PDPApi.md#getjobstatus) | **GET** /jobs/{jobId}/status | gets a job status
*TMPApi* | [**GetJob**](docs/TMPApi.md#getjob) | **GET** /jobs/{jobId} | gets a job
*TMPApi* | [**GetJobStatus**](docs/TMPApi.md#getjobstatus) | **GET** /jobs/{jobId}/status | gets a job status
*TMPApi* | [**SolveTMP**](docs/TMPApi.md#solvetmp) | **POST** /solve#TMP | solve a TMP problem
*VRPApi* | [**GetJob**](docs/VRPApi.md#getjob) | **GET** /jobs/{jobId} | gets a job
*VRPApi* | [**GetJobStatus**](docs/VRPApi.md#getjobstatus) | **GET** /jobs/{jobId}/status | gets a job status
*VRPApi* | [**SolveVRP**](docs/VRPApi.md#solvevrp) | **POST** /solve#VRP | solve a VRP problem

<a name="documentation-for-models"></a>
## Documentation for Models

 - [Model.Job](docs/Job.md)
 - [Model.Location](docs/Location.md)
 - [Model.Options](docs/Options.md)
 - [Model.Order](docs/Order.md)
 - [Model.OrderWindows](docs/OrderWindows.md)
 - [Model.Sales](docs/Sales.md)
 - [Model.Store](docs/Store.md)
 - [Model.TMP](docs/TMP.md)
 - [Model.VRP](docs/VRP.md)
 - [Model.Vehicle](docs/Vehicle.md)

<a name="documentation-for-authorization"></a>
## Documentation for Authorization

<a name="basicAuth"></a>
### basicAuth

- **Type**: HTTP basic authentication


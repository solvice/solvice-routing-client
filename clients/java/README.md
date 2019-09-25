# routing-client

OnRoute API
- API version: 1.1.3

No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)


*Automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen)*


## Requirements

Building the API client library requires:
1. Java 1.7+
2. Maven/Gradle

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>io.solvice</groupId>
  <artifactId>routing-client</artifactId>
  <version>0.9</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
compile "io.solvice:routing-client:0.9"
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/routing-client-0.9.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java
import io.solvice.routing.api.client.*;
import io.solvice.routing.api.client.auth.*;
import io.solvice.routing.api.client.model.*;
import io.solvice.routing.api.client.api.PdpApi;

import java.io.File;
import java.util.*;

public class PdpApiExample {

    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        PdpApi apiInstance = new PdpApi();
        UUID jobId = new UUID(); // UUID | The job ID.
        try {
            Job result = apiInstance.getJob(jobId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PdpApi#getJob");
            e.printStackTrace();
        }
    }
}
import io.solvice.routing.api.client.*;
import io.solvice.routing.api.client.auth.*;
import io.solvice.routing.api.client.model.*;
import io.solvice.routing.api.client.api.PdpApi;

import java.io.File;
import java.util.*;

public class PdpApiExample {

    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        PdpApi apiInstance = new PdpApi();
        String jobId = "jobId_example"; // String | The job ID.
        try {
            Job result = apiInstance.getJobStatus(jobId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PdpApi#getJobStatus");
            e.printStackTrace();
        }
    }
}
import io.solvice.routing.api.client.*;
import io.solvice.routing.api.client.auth.*;
import io.solvice.routing.api.client.model.*;
import io.solvice.routing.api.client.api.PdpApi;

import java.io.File;
import java.util.*;

public class PdpApiExample {

    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        PdpApi apiInstance = new PdpApi();
        UUID jobId = new UUID(); // UUID | The job ID.
        try {
            RoutingSolution result = apiInstance.getSolutionPDP(jobId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PdpApi#getSolutionPDP");
            e.printStackTrace();
        }
    }
}
import io.solvice.routing.api.client.*;
import io.solvice.routing.api.client.auth.*;
import io.solvice.routing.api.client.model.*;
import io.solvice.routing.api.client.api.PdpApi;

import java.io.File;
import java.util.*;

public class PdpApiExample {

    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        PdpApi apiInstance = new PdpApi();
        PDP body = new PDP(); // PDP | PDP problem solve request
        try {
            Job result = apiInstance.solvePDP(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PdpApi#solvePDP");
            e.printStackTrace();
        }
    }
}
```

## Documentation for API Endpoints

All URIs are relative to *https://api.solvice.io/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PdpApi* | [**getJob**](docs/PdpApi.md#getJob) | **GET** /jobs/{jobId} | Job
*PdpApi* | [**getJobStatus**](docs/PdpApi.md#getJobStatus) | **GET** /jobs/{jobId}/status | Status
*PdpApi* | [**getSolutionPDP**](docs/PdpApi.md#getSolutionPDP) | **GET** /jobs/{jobId}/solution#PDP | Solution PDP
*PdpApi* | [**solvePDP**](docs/PdpApi.md#solvePDP) | **POST** /solve#PDP | Solve a PDP problem
*PvrpApi* | [**solvePVRP**](docs/PvrpApi.md#solvePVRP) | **POST** /solve#PVRP | Solve a PVRP problem
*SolviceApiApi* | [**getJob**](docs/SolviceApiApi.md#getJob) | **GET** /jobs/{jobId} | Job
*SolviceApiApi* | [**getJobStatus**](docs/SolviceApiApi.md#getJobStatus) | **GET** /jobs/{jobId}/status | Status
*SolviceApiApi* | [**getSolution**](docs/SolviceApiApi.md#getSolution) | **GET** /jobs/{jobId}/solution | Solution
*SolviceApiApi* | [**getStats**](docs/SolviceApiApi.md#getStats) | **GET** /v1/stats/{jobId} | Statistics
*TmpApi* | [**getJob**](docs/TmpApi.md#getJob) | **GET** /jobs/{jobId} | Job
*TmpApi* | [**getJobStatus**](docs/TmpApi.md#getJobStatus) | **GET** /jobs/{jobId}/status | Status
*TmpApi* | [**solveTMP**](docs/TmpApi.md#solveTMP) | **POST** /solve#TMP | solve a TMP problem
*VrpApi* | [**getJob**](docs/VrpApi.md#getJob) | **GET** /jobs/{jobId} | Job
*VrpApi* | [**getJobStatus**](docs/VrpApi.md#getJobStatus) | **GET** /jobs/{jobId}/status | Status
*VrpApi* | [**getSolutionVrp**](docs/VrpApi.md#getSolutionVrp) | **GET** /jobs/{jobId}/solution#VRP | Solution VRP
*VrpApi* | [**solveVRP**](docs/VrpApi.md#solveVRP) | **POST** /solve#VRP | solve a VRP problem

## Documentation for Models

 - [ApiError](docs/ApiError.md)
 - [ApiErrorInner](docs/ApiErrorInner.md)
 - [InputError](docs/InputError.md)
 - [Job](docs/Job.md)
 - [Location](docs/Location.md)
 - [Options](docs/Options.md)
 - [Order](docs/Order.md)
 - [OrderDateWindows](docs/OrderDateWindows.md)
 - [OrderWindows](docs/OrderWindows.md)
 - [PDP](docs/PDP.md)
 - [PVRP](docs/PVRP.md)
 - [RoutingSolution](docs/RoutingSolution.md)
 - [Sales](docs/Sales.md)
 - [Solver](docs/Solver.md)
 - [Stats](docs/Stats.md)
 - [StatsConflicts](docs/StatsConflicts.md)
 - [StatsGoals](docs/StatsGoals.md)
 - [Status](docs/Status.md)
 - [Store](docs/Store.md)
 - [TMP](docs/TMP.md)
 - [VRP](docs/VRP.md)
 - [Vehicle](docs/Vehicle.md)
 - [VehicleBreaks](docs/VehicleBreaks.md)
 - [Visit](docs/Visit.md)

## Documentation for Authorization

Authentication schemes defined for the API:
### basicAuth

- **Type**: HTTP basic authentication


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author


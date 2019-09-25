/*
 * OnRoute API
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.1.3
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.solvice.routing.api.client.api;

import io.solvice.routing.api.client.ApiCallback;
import io.solvice.routing.api.client.ApiClient;
import io.solvice.routing.api.client.ApiException;
import io.solvice.routing.api.client.ApiResponse;
import io.solvice.routing.api.client.Configuration;
import io.solvice.routing.api.client.Pair;
import io.solvice.routing.api.client.ProgressRequestBody;
import io.solvice.routing.api.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import io.solvice.routing.api.client.model.InputError;
import io.solvice.routing.api.client.model.Job;
import io.solvice.routing.api.client.model.PDP;
import io.solvice.routing.api.client.model.RoutingSolution;
import java.util.UUID;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PdpApi {
    private ApiClient apiClient;

    public PdpApi() {
        this(Configuration.getDefaultApiClient());
    }

    public PdpApi(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return apiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    /**
     * Build call for getJobStatus
     * @param jobId The job ID. (required)
     * @param progressListener Progress listener
     * @param progressRequestListener Progress request listener
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public com.squareup.okhttp.Call getJobStatusCall(String jobId, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        Object localVarPostBody = null;
        
        // create path and map variables
        String localVarPath = "/jobs/{jobId}/status"
            .replaceAll("\\{" + "jobId" + "\\}", apiClient.escapeString(jobId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();

        Map<String, String> localVarHeaderParams = new HashMap<String, String>();

        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) localVarHeaderParams.put("Accept", localVarAccept);

        final String[] localVarContentTypes = {
            
        };
        final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);
        localVarHeaderParams.put("Content-Type", localVarContentType);

        if(progressListener != null) {
            apiClient.getHttpClient().networkInterceptors().add(new com.squareup.okhttp.Interceptor() {
                @Override
                public com.squareup.okhttp.Response intercept(com.squareup.okhttp.Interceptor.Chain chain) throws IOException {
                    com.squareup.okhttp.Response originalResponse = chain.proceed(chain.request());
                    return originalResponse.newBuilder()
                    .body(new ProgressResponseBody(originalResponse.body(), progressListener))
                    .build();
                }
            });
        }

        String[] localVarAuthNames = new String[] { "basicAuth" };
        return apiClient.buildCall(localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarAuthNames, progressRequestListener);
    }
    
    @SuppressWarnings("rawtypes")
    private com.squareup.okhttp.Call getJobStatusValidateBeforeCall(String jobId, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        // verify the required parameter 'jobId' is set
        if (jobId == null) {
            throw new ApiException("Missing the required parameter 'jobId' when calling getJobStatus(Async)");
        }
        
        com.squareup.okhttp.Call call = getJobStatusCall(jobId, progressListener, progressRequestListener);
        return call;

        
        
        
        
    }

    /**
     * Status
     * Retrieve a specific job status
     * @param jobId The job ID. (required)
     * @return Job
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public Job getJobStatus(String jobId) throws ApiException {
        ApiResponse<Job> resp = getJobStatusWithHttpInfo(jobId);
        return resp.getData();
    }

    /**
     * Status
     * Retrieve a specific job status
     * @param jobId The job ID. (required)
     * @return ApiResponse&lt;Job&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<Job> getJobStatusWithHttpInfo(String jobId) throws ApiException {
        com.squareup.okhttp.Call call = getJobStatusValidateBeforeCall(jobId, null, null);
        Type localVarReturnType = new TypeToken<Job>(){}.getType();
        return apiClient.execute(call, localVarReturnType);
    }

    /**
     * Status (asynchronously)
     * Retrieve a specific job status
     * @param jobId The job ID. (required)
     * @param callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public com.squareup.okhttp.Call getJobStatusAsync(String jobId, final ApiCallback<Job> callback) throws ApiException {

        ProgressResponseBody.ProgressListener progressListener = null;
        ProgressRequestBody.ProgressRequestListener progressRequestListener = null;

        if (callback != null) {
            progressListener = new ProgressResponseBody.ProgressListener() {
                @Override
                public void update(long bytesRead, long contentLength, boolean done) {
                    callback.onDownloadProgress(bytesRead, contentLength, done);
                }
            };

            progressRequestListener = new ProgressRequestBody.ProgressRequestListener() {
                @Override
                public void onRequestProgress(long bytesWritten, long contentLength, boolean done) {
                    callback.onUploadProgress(bytesWritten, contentLength, done);
                }
            };
        }

        com.squareup.okhttp.Call call = getJobStatusValidateBeforeCall(jobId, progressListener, progressRequestListener);
        Type localVarReturnType = new TypeToken<Job>(){}.getType();
        apiClient.executeAsync(call, localVarReturnType, callback);
        return call;
    }
    /**
     * Build call for getSolutionPDP
     * @param jobId The job ID. (required)
     * @param progressListener Progress listener
     * @param progressRequestListener Progress request listener
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public com.squareup.okhttp.Call getSolutionPDPCall(UUID jobId, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        Object localVarPostBody = null;
        
        // create path and map variables
        String localVarPath = "/jobs/{jobId}/solution#PDP"
            .replaceAll("\\{" + "jobId" + "\\}", apiClient.escapeString(jobId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();

        Map<String, String> localVarHeaderParams = new HashMap<String, String>();

        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) localVarHeaderParams.put("Accept", localVarAccept);

        final String[] localVarContentTypes = {
            
        };
        final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);
        localVarHeaderParams.put("Content-Type", localVarContentType);

        if(progressListener != null) {
            apiClient.getHttpClient().networkInterceptors().add(new com.squareup.okhttp.Interceptor() {
                @Override
                public com.squareup.okhttp.Response intercept(com.squareup.okhttp.Interceptor.Chain chain) throws IOException {
                    com.squareup.okhttp.Response originalResponse = chain.proceed(chain.request());
                    return originalResponse.newBuilder()
                    .body(new ProgressResponseBody(originalResponse.body(), progressListener))
                    .build();
                }
            });
        }

        String[] localVarAuthNames = new String[] { "basicAuth" };
        return apiClient.buildCall(localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarAuthNames, progressRequestListener);
    }
    
    @SuppressWarnings("rawtypes")
    private com.squareup.okhttp.Call getSolutionPDPValidateBeforeCall(UUID jobId, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        // verify the required parameter 'jobId' is set
        if (jobId == null) {
            throw new ApiException("Missing the required parameter 'jobId' when calling getSolutionPDP(Async)");
        }
        
        com.squareup.okhttp.Call call = getSolutionPDPCall(jobId, progressListener, progressRequestListener);
        return call;

        
        
        
        
    }

    /**
     * Solution PDP
     * Returns the actual solution of the PDP. Only present when the status is &#x60;SOLVED&#x60;.
     * @param jobId The job ID. (required)
     * @return RoutingSolution
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public RoutingSolution getSolutionPDP(UUID jobId) throws ApiException {
        ApiResponse<RoutingSolution> resp = getSolutionPDPWithHttpInfo(jobId);
        return resp.getData();
    }

    /**
     * Solution PDP
     * Returns the actual solution of the PDP. Only present when the status is &#x60;SOLVED&#x60;.
     * @param jobId The job ID. (required)
     * @return ApiResponse&lt;RoutingSolution&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<RoutingSolution> getSolutionPDPWithHttpInfo(UUID jobId) throws ApiException {
        com.squareup.okhttp.Call call = getSolutionPDPValidateBeforeCall(jobId, null, null);
        Type localVarReturnType = new TypeToken<RoutingSolution>(){}.getType();
        return apiClient.execute(call, localVarReturnType);
    }

    /**
     * Solution PDP (asynchronously)
     * Returns the actual solution of the PDP. Only present when the status is &#x60;SOLVED&#x60;.
     * @param jobId The job ID. (required)
     * @param callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public com.squareup.okhttp.Call getSolutionPDPAsync(UUID jobId, final ApiCallback<RoutingSolution> callback) throws ApiException {

        ProgressResponseBody.ProgressListener progressListener = null;
        ProgressRequestBody.ProgressRequestListener progressRequestListener = null;

        if (callback != null) {
            progressListener = new ProgressResponseBody.ProgressListener() {
                @Override
                public void update(long bytesRead, long contentLength, boolean done) {
                    callback.onDownloadProgress(bytesRead, contentLength, done);
                }
            };

            progressRequestListener = new ProgressRequestBody.ProgressRequestListener() {
                @Override
                public void onRequestProgress(long bytesWritten, long contentLength, boolean done) {
                    callback.onUploadProgress(bytesWritten, contentLength, done);
                }
            };
        }

        com.squareup.okhttp.Call call = getSolutionPDPValidateBeforeCall(jobId, progressListener, progressRequestListener);
        Type localVarReturnType = new TypeToken<RoutingSolution>(){}.getType();
        apiClient.executeAsync(call, localVarReturnType, callback);
        return call;
    }
    /**
     * Build call for solvePDP
     * @param body PDP problem solve request (optional)
     * @param progressListener Progress listener
     * @param progressRequestListener Progress request listener
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public com.squareup.okhttp.Call solvePDPCall(PDP body, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        Object localVarPostBody = body;
        
        // create path and map variables
        String localVarPath = "/solve#PDP";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();

        Map<String, String> localVarHeaderParams = new HashMap<String, String>();

        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) localVarHeaderParams.put("Accept", localVarAccept);

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);
        localVarHeaderParams.put("Content-Type", localVarContentType);

        if(progressListener != null) {
            apiClient.getHttpClient().networkInterceptors().add(new com.squareup.okhttp.Interceptor() {
                @Override
                public com.squareup.okhttp.Response intercept(com.squareup.okhttp.Interceptor.Chain chain) throws IOException {
                    com.squareup.okhttp.Response originalResponse = chain.proceed(chain.request());
                    return originalResponse.newBuilder()
                    .body(new ProgressResponseBody(originalResponse.body(), progressListener))
                    .build();
                }
            });
        }

        String[] localVarAuthNames = new String[] { "basicAuth" };
        return apiClient.buildCall(localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarAuthNames, progressRequestListener);
    }
    
    @SuppressWarnings("rawtypes")
    private com.squareup.okhttp.Call solvePDPValidateBeforeCall(PDP body, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        
        com.squareup.okhttp.Call call = solvePDPCall(body, progressListener, progressRequestListener);
        return call;

        
        
        
        
    }

    /**
     * Solve a PDP problem
     * Pickup and delivery problems
     * @param body PDP problem solve request (optional)
     * @return Job
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public Job solvePDP(PDP body) throws ApiException {
        ApiResponse<Job> resp = solvePDPWithHttpInfo(body);
        return resp.getData();
    }

    /**
     * Solve a PDP problem
     * Pickup and delivery problems
     * @param body PDP problem solve request (optional)
     * @return ApiResponse&lt;Job&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<Job> solvePDPWithHttpInfo(PDP body) throws ApiException {
        com.squareup.okhttp.Call call = solvePDPValidateBeforeCall(body, null, null);
        Type localVarReturnType = new TypeToken<Job>(){}.getType();
        return apiClient.execute(call, localVarReturnType);
    }

    /**
     * Solve a PDP problem (asynchronously)
     * Pickup and delivery problems
     * @param body PDP problem solve request (optional)
     * @param callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public com.squareup.okhttp.Call solvePDPAsync(PDP body, final ApiCallback<Job> callback) throws ApiException {

        ProgressResponseBody.ProgressListener progressListener = null;
        ProgressRequestBody.ProgressRequestListener progressRequestListener = null;

        if (callback != null) {
            progressListener = new ProgressResponseBody.ProgressListener() {
                @Override
                public void update(long bytesRead, long contentLength, boolean done) {
                    callback.onDownloadProgress(bytesRead, contentLength, done);
                }
            };

            progressRequestListener = new ProgressRequestBody.ProgressRequestListener() {
                @Override
                public void onRequestProgress(long bytesWritten, long contentLength, boolean done) {
                    callback.onUploadProgress(bytesWritten, contentLength, done);
                }
            };
        }

        com.squareup.okhttp.Call call = solvePDPValidateBeforeCall(body, progressListener, progressRequestListener);
        Type localVarReturnType = new TypeToken<Job>(){}.getType();
        apiClient.executeAsync(call, localVarReturnType, callback);
        return call;
    }
}

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

import io.solvice.routing.api.client.ApiException;
import io.solvice.routing.api.client.model.Job;
import io.solvice.routing.api.client.model.RoutingSolution;
import java.util.UUID;
import io.solvice.routing.api.client.model.VRP;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for VrpApi
 */
@Ignore
public class VrpApiTest {

    private final VrpApi api = new VrpApi();

    /**
     * Job
     *
     * When posting a new solve request, this job can be checked again under this endpoint. In fact, it should be the entire request posted as-is.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getJobTest() throws ApiException {
        UUID jobId = null;
        Job response = api.getJob(jobId);

        // TODO: test validations
    }
    /**
     * Status
     *
     * Retrieve a specific job status
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getJobStatusTest() throws ApiException {
        String jobId = null;
        Job response = api.getJobStatus(jobId);

        // TODO: test validations
    }
    /**
     * Solution VRP
     *
     * Returns the actual solution of the VRP. Only present when the status is &#x60;SOLVED&#x60;.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getSolutionVrpTest() throws ApiException {
        UUID jobId = null;
        RoutingSolution response = api.getSolutionVrp(jobId);

        // TODO: test validations
    }
    /**
     * solve a VRP problem
     *
     * Adds an item to the system
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void solveVRPTest() throws ApiException {
        VRP body = null;
        Job response = api.solveVRP(body);

        // TODO: test validations
    }
}

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
import io.solvice.routing.api.client.model.InputError;
import io.solvice.routing.api.client.model.Job;
import io.solvice.routing.api.client.model.TMP;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for TmpApi
 */
@Ignore
public class TmpApiTest {

    private final TmpApi api = new TmpApi();

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
     * solve a TMP problem
     *
     * Solves a TMP problem
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void solveTMPTest() throws ApiException {
        TMP body = null;
        Job response = api.solveTMP(body);

        // TODO: test validations
    }
}

/* 
 * Solvice API
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.0.0-oas3
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Reflection;
using RestSharp;
using NUnit.Framework;

using SolviceRoutingClient.Client;
using SolviceRoutingClient.Api;
using SolviceRoutingClient.Model;

namespace SolviceRoutingClient.Test
{
    /// <summary>
    ///  Class for testing VRPApi
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by Swagger Codegen.
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    [TestFixture]
    public class VRPApiTests
    {
        private VRPApi instance;

        /// <summary>
        /// Setup before each unit test
        /// </summary>
        [SetUp]
        public void Init()
        {
            instance = new VRPApi();
        }

        /// <summary>
        /// Clean up after each unit test
        /// </summary>
        [TearDown]
        public void Cleanup()
        {

        }

        /// <summary>
        /// Test an instance of VRPApi
        /// </summary>
        [Test]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsInstanceOfType' VRPApi
            //Assert.IsInstanceOfType(typeof(VRPApi), instance, "instance is a VRPApi");
        }

        /// <summary>
        /// Test GetJob
        /// </summary>
        [Test]
        public void GetJobTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string jobId = null;
            //var response = instance.GetJob(jobId);
            //Assert.IsInstanceOf<Job> (response, "response is Job");
        }
        /// <summary>
        /// Test GetJobStatus
        /// </summary>
        [Test]
        public void GetJobStatusTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string jobId = null;
            //var response = instance.GetJobStatus(jobId);
            //Assert.IsInstanceOf<Job> (response, "response is Job");
        }
        /// <summary>
        /// Test SolveVRP
        /// </summary>
        [Test]
        public void SolveVRPTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //VRP body = null;
            //instance.SolveVRP(body);
            
        }
    }

}
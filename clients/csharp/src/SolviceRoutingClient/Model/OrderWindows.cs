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
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = SolviceRoutingClient.Client.SwaggerDateConverter;

namespace SolviceRoutingClient.Model
{
    /// <summary>
    /// OrderWindows
    /// </summary>
    [DataContract]
        public partial class OrderWindows :  IEquatable<OrderWindows>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="OrderWindows" /> class.
        /// </summary>
        /// <param name="">.</param>
        /// <param name="">.</param>
        /// <param name="">.</param>
        public OrderWindows(int?  = default(int?), int?  = default(int?), bool?  = default(bool?))
        {
            this.Starttime = ;
            this.Endtime = ;
            this.Hard = ;
        }
        
        /// <summary>
        /// Gets or Sets Starttime
        /// </summary>
        [DataMember(Name="starttime", EmitDefaultValue=false)]
        public int? Starttime { get; set; }

        /// <summary>
        /// Gets or Sets Endtime
        /// </summary>
        [DataMember(Name="endtime", EmitDefaultValue=false)]
        public int? Endtime { get; set; }

        /// <summary>
        /// Gets or Sets Hard
        /// </summary>
        [DataMember(Name="hard", EmitDefaultValue=false)]
        public bool? Hard { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class OrderWindows {\n");
            sb.Append("  Starttime: ").Append(Starttime).Append("\n");
            sb.Append("  Endtime: ").Append(Endtime).Append("\n");
            sb.Append("  Hard: ").Append(Hard).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as OrderWindows);
        }

        /// <summary>
        /// Returns true if OrderWindows instances are equal
        /// </summary>
        /// <param name="input">Instance of OrderWindows to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(OrderWindows input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Starttime == input.Starttime ||
                    (this.Starttime != null &&
                    this.Starttime.Equals(input.Starttime))
                ) && 
                (
                    this.Endtime == input.Endtime ||
                    (this.Endtime != null &&
                    this.Endtime.Equals(input.Endtime))
                ) && 
                (
                    this.Hard == input.Hard ||
                    (this.Hard != null &&
                    this.Hard.Equals(input.Hard))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Starttime != null)
                    hashCode = hashCode * 59 + this.Starttime.GetHashCode();
                if (this.Endtime != null)
                    hashCode = hashCode * 59 + this.Endtime.GetHashCode();
                if (this.Hard != null)
                    hashCode = hashCode * 59 + this.Hard.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }
}

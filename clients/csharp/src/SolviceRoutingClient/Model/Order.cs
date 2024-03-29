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
    /// Order
    /// </summary>
    [DataContract]
        public partial class Order :  IEquatable<Order>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Order" /> class.
        /// </summary>
        /// <param name=""> (required).</param>
        /// <param name=""> (required).</param>
        /// <param name="">.</param>
        /// <param name="">.</param>
        /// <param name="">.</param>
        /// <param name="">.</param>
        /// <param name="">.</param>
        public Order(string  = default(string), string  = default(string), BigDecimal  = default(BigDecimal), BigDecimal  = default(BigDecimal), BigDecimal  = default(BigDecimal), List<string>  = default(List<string>), List<OrderWindows>  = default(List<OrderWindows>))
        {
            // to ensure "" is required (not null)
            if ( == null)
            {
                throw new InvalidDataException(" is a required property for Order and cannot be null");
            }
            else
            {
                this.Name = ;
            }
            // to ensure "" is required (not null)
            if ( == null)
            {
                throw new InvalidDataException(" is a required property for Order and cannot be null");
            }
            else
            {
                this.Location = ;
            }
            this.Duration = ;
            this.Demand = ;
            this.Demand2 = ;
            this.Type = ;
            this.Windows = ;
        }
        
        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        [DataMember(Name="name", EmitDefaultValue=false)]
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets Location
        /// </summary>
        [DataMember(Name="location", EmitDefaultValue=false)]
        public string Location { get; set; }

        /// <summary>
        /// Gets or Sets Duration
        /// </summary>
        [DataMember(Name="duration", EmitDefaultValue=false)]
        public BigDecimal Duration { get; set; }

        /// <summary>
        /// Gets or Sets Demand
        /// </summary>
        [DataMember(Name="demand", EmitDefaultValue=false)]
        public BigDecimal Demand { get; set; }

        /// <summary>
        /// Gets or Sets Demand2
        /// </summary>
        [DataMember(Name="demand2", EmitDefaultValue=false)]
        public BigDecimal Demand2 { get; set; }

        /// <summary>
        /// Gets or Sets Type
        /// </summary>
        [DataMember(Name="type", EmitDefaultValue=false)]
        public List<string> Type { get; set; }

        /// <summary>
        /// Gets or Sets Windows
        /// </summary>
        [DataMember(Name="windows", EmitDefaultValue=false)]
        public List<OrderWindows> Windows { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class Order {\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  Location: ").Append(Location).Append("\n");
            sb.Append("  Duration: ").Append(Duration).Append("\n");
            sb.Append("  Demand: ").Append(Demand).Append("\n");
            sb.Append("  Demand2: ").Append(Demand2).Append("\n");
            sb.Append("  Type: ").Append(Type).Append("\n");
            sb.Append("  Windows: ").Append(Windows).Append("\n");
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
            return this.Equals(input as Order);
        }

        /// <summary>
        /// Returns true if Order instances are equal
        /// </summary>
        /// <param name="input">Instance of Order to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(Order input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.Location == input.Location ||
                    (this.Location != null &&
                    this.Location.Equals(input.Location))
                ) && 
                (
                    this.Duration == input.Duration ||
                    (this.Duration != null &&
                    this.Duration.Equals(input.Duration))
                ) && 
                (
                    this.Demand == input.Demand ||
                    (this.Demand != null &&
                    this.Demand.Equals(input.Demand))
                ) && 
                (
                    this.Demand2 == input.Demand2 ||
                    (this.Demand2 != null &&
                    this.Demand2.Equals(input.Demand2))
                ) && 
                (
                    this.Type == input.Type ||
                    this.Type != null &&
                    this.Type.SequenceEqual(input.Type)
                ) && 
                (
                    this.Windows == input.Windows ||
                    this.Windows != null &&
                    this.Windows.SequenceEqual(input.Windows)
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
                if (this.Name != null)
                    hashCode = hashCode * 59 + this.Name.GetHashCode();
                if (this.Location != null)
                    hashCode = hashCode * 59 + this.Location.GetHashCode();
                if (this.Duration != null)
                    hashCode = hashCode * 59 + this.Duration.GetHashCode();
                if (this.Demand != null)
                    hashCode = hashCode * 59 + this.Demand.GetHashCode();
                if (this.Demand2 != null)
                    hashCode = hashCode * 59 + this.Demand2.GetHashCode();
                if (this.Type != null)
                    hashCode = hashCode * 59 + this.Type.GetHashCode();
                if (this.Windows != null)
                    hashCode = hashCode * 59 + this.Windows.GetHashCode();
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

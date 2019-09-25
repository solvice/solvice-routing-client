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

package io.solvice.routing.api.client.model;

import java.util.Objects;
import io.swagger.v3.oas.annotations.media.Schema;
import com.google.gson.annotations.SerializedName;

import java.io.IOException;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;

/**
 * Required solver enum definition. Please specify.
 */
@JsonAdapter(Solver.Adapter.class)
public enum Solver {
  VRP("VRP"),
  PDP("PDP"),
  PVRP("PVRP");

  private String value;

  Solver(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static Solver fromValue(String text) {
    for (Solver b : Solver.values()) {
      if (String.valueOf(b.value).equals(text)) {
        return b;
      }
    }
    return null;
  }

  public static class Adapter extends TypeAdapter<Solver> {
    @Override
    public void write(final JsonWriter jsonWriter, final Solver enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public Solver read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return Solver.fromValue(String.valueOf(value));
    }
  }
}

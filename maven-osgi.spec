%global pkg_name maven-osgi
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        0.2.0
Release:        7.9%{?dist}
# Maven-shared defines maven-osgi version as 0.3.0
Epoch:          1
Summary:        Library for Maven-OSGi integration
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-osgi
BuildArch:      noarch

# svn export http://svn.apache.org/repos/asf/maven/shared/tags/maven-osgi-0.2.0 maven-osgi-0.2.0
# find -name *.jar -delete
# tar caf maven-osgi-0.2.0.tar.xz maven-osgi-0.2.0/
Source0:        %{pkg_name}-%{version}.tar.xz
# ASL mandates that the licence file be included in redistributed source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix}mvn(biz.aQute:bndlib)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-plugin-testing-harness)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-project)


%description
Library for Maven-OSGi integration.

This is a replacement package for maven-shared-osgi

%package javadoc
Summary:        Javadoc for %{pkg_name}
    
%description javadoc
API documentation for %{pkg_name}.


%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
cp -p %{SOURCE1} LICENSE

# Replace plexus-maven-plugin with plexus-component-metadata
%pom_xpath_set "pom:plugin[pom:artifactId[text()='plexus-maven-plugin']]//pom:goal[text()='descriptor']" generate-metadata
%pom_xpath_set "pom:artifactId[text()='plexus-maven-plugin']" plexus-component-metadata
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
# Tests depend on binary JARs which were removed from sources
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE


%changelog
* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.0-7.9
- Add directory ownership on %%{_mavenpomdir} subdir

* Wed Jan 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.0-7.8
- Fix BR on maven-shared POM

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1:0.2.0-7.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1:0.2.0-7.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.0-7.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.0-7.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.0-7.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.0-7.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.0-7.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.0-7.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:0.2.0-7
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.0-6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon May 27 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.0-5
- Build with xmvn
- Remove bundled test JARs from sources
- Use POM macros instead of sed

* Wed Feb 20 2013 Tomas Radej <tradej@redhat.com> - 1:0.2.0-4
- Added B/R on maven-shared and maven-local

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 11 2013 Tomas Radej <tradej@redhat.com> - 1:0.2.0-2
- Fixed Provides/Obsoletes

* Mon Jan 07 2013 Tomas Radej <tradej@redhat.com> - 1:0.2.0-1
- Initial version

